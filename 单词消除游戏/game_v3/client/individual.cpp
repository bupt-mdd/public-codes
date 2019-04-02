#include <Winsock2.h>
#include<iostream>
#include<fstream>
#include<string>
#include<iomanip>
#include<windows.h>
#include"mylib.h"
#include"individual.h"
#pragma comment(lib,"ws2_32.lib")
using namespace std;

void individual::change(int role, int pass_num, int cur_experience)
{
	int command;
	char recvebuf[BUF_SIZE], sendbuf[BUF_SIZE] = { "\0" };

	ZeroMemory(sendbuf, BUF_SIZE);       //向服务器发送请求
	command = CHANGE;
	memcpy(sendbuf, &command, 4);
	int retVal = send(client, sendbuf, strlen(sendbuf), 0);

	ZeroMemory(recvebuf, BUF_SIZE);
	recv(client, recvebuf, BUF_SIZE, 0);
	if (recvebuf[0] == 'Y')
	{
		que_or_passnum = pass_num;
		if ((cur_experience + user_experience) >= 0)//保证等级不减，经验不会为负数。 是为挑战赛做准备
		{
			user_experience = user_experience + cur_experience;
		}
		else
			user_experience = 0;

		if (user_experience >= ((user_rank + 1)*INC_RANK_RATIO))//当经验满足要求后，会进行升级
		{
			user_experience = user_experience - ((user_rank + 1)*INC_RANK_RATIO);
			user_rank++;
		}
		ZeroMemory(sendbuf, BUF_SIZE);
		memcpy(sendbuf, &role, 4);
		send(client, sendbuf, strlen(sendbuf), 0);
	
		recv(client, recvebuf, BUF_SIZE, 0);
		ZeroMemory(sendbuf, BUF_SIZE);
		pass_num++;
		memcpy(sendbuf, &pass_num, 4);
		send(client, sendbuf, strlen(sendbuf), 0);
		recv(client, recvebuf, BUF_SIZE, 0);

		ZeroMemory(sendbuf, BUF_SIZE);
		cur_experience++;
		memcpy(sendbuf, &cur_experience, 4);
		send(client, sendbuf, strlen(sendbuf), 0);
		ZeroMemory(recvebuf, BUF_SIZE);
		recv(client, recvebuf, BUF_SIZE, 0);          //同时将相关信息发送给服务器，在服务器端口对玩家经验等信息进行修改

		if (recvebuf[0] != 'Y')
		{
			cout << "服务器连接出现问题" << endl;
		}
	}
	else
	{
		cout << "服务器繁忙，请稍后再试" << endl;
		ZeroMemory(sendbuf, BUF_SIZE);
		sendbuf[0] = '*';
		send(client, sendbuf, strlen(sendbuf), 0);
	}
}

void individual::search_All_individual()       //搜索输出当前该游戏所注册的所有的玩家
{
	int command;
	char recvebuf[BUF_SIZE], sendbuf[BUF_SIZE] = { "\0" };

	ZeroMemory(sendbuf, BUF_SIZE);       //向服务器发送请求
	command = SEARCH_ALL;
	memcpy(sendbuf, &command, 4);
	send(client, sendbuf, strlen(sendbuf), 0);

	ZeroMemory(recvebuf, BUF_SIZE);
	recv(client, recvebuf, BUF_SIZE, 0);
	if (recvebuf[0] == 'Y')
	{
		cout << "闯关者信息"<<endl;      //输出闯关者的所有信息

		cout<< setw(PROPER_NUM) << setiosflags(ios::left) << setfill(' ') << "账号为："
			<< setw(PROPER_NUM) << setiosflags(ios::left) << setfill(' ') << "玩家名为:"
			<< setw(PROPER_NUM/2) << setiosflags(ios::right) << setfill(' ') << "等级为:"
			<< setw(PROPER_NUM/2) << setiosflags(ios::right) << setfill(' ') << "经验为:"
			<< setw(PROPER_NUM/2) << setiosflags(ios::right) << setfill(' ') << "闯关数:" << endl;
		int i = 0;
		ZeroMemory(sendbuf, BUF_SIZE);
		sendbuf[0] = 'Y';
		send(client, sendbuf, strlen(sendbuf), 0);
		ZeroMemory(recvebuf, BUF_SIZE);
		recv(client, recvebuf, BUF_SIZE, 0);

		while (recvebuf[0] != 'N')
		{
			
			if ((i % 5) < 2)
			{
				cout << setw(PROPER_NUM) << setiosflags(ios::left) << setfill(' ') << recvebuf;
			}
			else 
			{
				int j = 0;
				memcpy(&j, recvebuf, 4);
				cout << setw(PROPER_NUM/2) << setiosflags(ios::right) << setfill(' ') << j-1;
			}
			i++;
			if ((i % 5) == 0)
				cout << endl;

			ZeroMemory(sendbuf, BUF_SIZE);
			sendbuf[0] = 'Y';
			send(client, sendbuf, strlen(sendbuf), 0);
			ZeroMemory(recvebuf, BUF_SIZE);
			recv(client, recvebuf, BUF_SIZE, 0);
		}

		ZeroMemory(sendbuf, BUF_SIZE);
		sendbuf[0] = 'Y';
		send(client, sendbuf, strlen(sendbuf), 0);
		cout << "出题者信息" << endl;       //输出出题者的所有的信息
		ZeroMemory(recvebuf, BUF_SIZE);
		recv(client, recvebuf, BUF_SIZE, 0);
		cout << setw(PROPER_NUM) << setiosflags(ios::left) << setfill(' ') << "账号为："
			 << setw(PROPER_NUM) << setiosflags(ios::left) << setfill(' ') << "玩家名为:"
			 << setw(PROPER_NUM/2) << setiosflags(ios::right) << setfill(' ') << "等级为:"
			 << setw(PROPER_NUM/2) << setiosflags(ios::right) << setfill(' ') << "经验为:"
			 << setw(PROPER_NUM/2) << setiosflags(ios::right) << setfill(' ') << "出题数:" << endl;

		i = 0;
		ZeroMemory(sendbuf, BUF_SIZE);
		sendbuf[0] = 'Y';
		send(client, sendbuf, strlen(sendbuf), 0);
		ZeroMemory(recvebuf, BUF_SIZE);
		recv(client, recvebuf, BUF_SIZE, 0);

		while (recvebuf[0] != 'N')
		{

			if ((i % 5) < 2)
			{
				cout << setw(PROPER_NUM) << setiosflags(ios::left) << setfill(' ') << recvebuf;
			}
			else
			{
				int j = 0;
				memcpy(&j, recvebuf, 4);
				cout << setw(PROPER_NUM / 2) << setiosflags(ios::right) << setfill(' ') << j - 1;
			}
			i++;
			if ((i % 5) == 0)
				cout << endl;

			ZeroMemory(sendbuf, BUF_SIZE);
			sendbuf[0] = 'Y';
			send(client, sendbuf, strlen(sendbuf), 0);
			ZeroMemory(recvebuf, BUF_SIZE);
			recv(client, recvebuf, BUF_SIZE, 0);
		}
	}
	else
	{
		cout << "服务器繁忙，请稍后再试" << endl;
		ZeroMemory(sendbuf, BUF_SIZE);
		sendbuf[0] = '*';
		send(client, sendbuf, strlen(sendbuf), 0);
	}
}

void individual::search_individual()   //按照属性进行查询
{
	int in_command;
	char cmd_str[MAX_ARRAY_NUM];
	char cmd;
	system("cls");
	cout << "********************************************************" << endl;
	cout << "*                    请选择查询的标准                  *" << endl;
	cout << "*    1按账号查询                2按姓名查询            *" << endl;
	cout << "*    3按等级查询                4按经验查询            *" << endl;
	cout << "*    5按出题(关卡)查询          6退出                  *" << endl;
	cout << "********************************************************" << endl;
	cin >> cmd_str;
	cmd = cmd_str[0];
	in_command = transfer_cmd(cmd);

	char information[PROPER_NUM] = { '\0' };
	while (in_command != 6)
	{
		system("cls");
		switch (in_command)
		{
		case 1:
			search(1);
			break;
		case 2:
			search(2);
			break;
		case 3:
			search(3 );
			break;
		case 4:
			search(4);
			break;
		case 5:
			search(5);
			break;
		default: break;
		}
		cout << "********************************************************" << endl;
		cout << "*                    请选择查询的标准                  *" << endl;
		cout << "*    1按账号查询                2按姓名查询            *" << endl;
		cout << "*    3按等级查询                4按经验查询            *" << endl;
		cout << "*    5按出题(关卡)查询          6退出                  *" << endl;
		cout << "********************************************************" << endl;
		cin >> cmd_str;
		cmd = cmd_str[0];
		in_command = transfer_cmd(cmd);
	}
	system("cls");
}

void individual::search(int num)     //暗属性查询时，改程序与服务器发生信息交换和输出
{
	int command;
	char recvebuf[BUF_SIZE], sendbuf[BUF_SIZE] = { "\0" };
	int in_find_inf;

	ZeroMemory(sendbuf, BUF_SIZE);
	command = SEARCH_ONES;
	memcpy(sendbuf, &command, 4);
	send(client, sendbuf, strlen(sendbuf), 0);//查询命令传过去
	ZeroMemory(recvebuf, BUF_SIZE);
	recv(client, recvebuf, BUF_SIZE, 0);

	ZeroMemory(sendbuf, BUF_SIZE);
	memcpy(sendbuf, &num, 4);
	send(client, sendbuf, strlen(sendbuf), 0);//将内部小命令传过去
	ZeroMemory(recvebuf, BUF_SIZE);
	recv(client, recvebuf, BUF_SIZE, 0);

	if (recvebuf[0] == 'Y')
	{
		switch (num)
		{
		case 1:

			cout << "请输入查询者的账号" << endl;
			ZeroMemory(sendbuf, BUF_SIZE);
			cin >> sendbuf;
			send(client, sendbuf, strlen(sendbuf), 0);
			ZeroMemory(recvebuf, BUF_SIZE);
			recv(client, recvebuf, BUF_SIZE, 0);

			break;
		case 2:
			cout << "请输入查询者的姓名" << endl;
			ZeroMemory(sendbuf, BUF_SIZE);
			cin >> sendbuf;
			send(client, sendbuf, strlen(sendbuf), 0);
			ZeroMemory(recvebuf, BUF_SIZE);
			recv(client, recvebuf, BUF_SIZE, 0);

			break;
		case 3:
			cout << "请输入查询者的等级" << endl;
			ZeroMemory(sendbuf, BUF_SIZE);
			cin >> in_find_inf;
			in_find_inf++;
			memcpy(sendbuf, &in_find_inf, 4);
			send(client, sendbuf, strlen(sendbuf), 0);
			ZeroMemory(recvebuf, BUF_SIZE);
			recv(client, recvebuf, BUF_SIZE, 0);

			break;
		case 4:
			cout << "请输入查询者的经验" << endl;
			ZeroMemory(sendbuf, BUF_SIZE);
			cin >> in_find_inf;
			in_find_inf++;
			memcpy(sendbuf,&in_find_inf,4);
			send(client, sendbuf, strlen(sendbuf), 0);
			ZeroMemory(recvebuf, BUF_SIZE);
			recv(client, recvebuf, BUF_SIZE, 0);

			break;
		case 5:
			cout << "请输入查询账号的关卡（出题数）" << endl;
			ZeroMemory(sendbuf, BUF_SIZE);
			cin >> in_find_inf;
			in_find_inf++;
			memcpy(sendbuf, &in_find_inf, 4);
			send(client, sendbuf, strlen(sendbuf), 0);
			ZeroMemory(recvebuf, BUF_SIZE);
			recv(client, recvebuf, BUF_SIZE, 0);

			break;
		default: break;
		}
		cout << "对闯关者的查询信息如下" << endl;

		if ((recvebuf[0] == '-') && (recvebuf[1] == '>'))
		{
			cout << "无该信息对应的闯关者" << endl;
		}
		else
		{
			cout << setw(PROPER_NUM) << setiosflags(ios::left) << setfill(' ') << "账号为："
				<< setw(PROPER_NUM) << setiosflags(ios::left) << setfill(' ') << "玩家名为:"
				<< setw(PROPER_NUM / 2) << setiosflags(ios::right) << setfill(' ') << "等级为:"
				<< setw(PROPER_NUM / 2) << setiosflags(ios::right) << setfill(' ') << "经验为:"
				<< setw(PROPER_NUM / 2) << setiosflags(ios::right) << setfill(' ') << "闯关数:" << endl;
			int i = 0;
			while ((recvebuf[0] != '-') || (recvebuf[1] != '>'))
			{
				if ((i % 5) < 2)
				{
					cout << setw(PROPER_NUM) << setiosflags(ios::left) << setfill(' ') << recvebuf;
				}
				else
				{
					int j = 0;
					memcpy(&j, recvebuf, 4);
					cout << setw(PROPER_NUM / 2) << setiosflags(ios::right) << setfill(' ') << j - 1;
				}
				i++;
				if ((i % 5) == 0)
					cout << endl;

				ZeroMemory(sendbuf, BUF_SIZE);
				sendbuf[0] = 'Y';
				send(client, sendbuf, strlen(sendbuf), 0);
				ZeroMemory(recvebuf, BUF_SIZE);
				recv(client, recvebuf, BUF_SIZE, 0);
			}
		}

		ZeroMemory(sendbuf, BUF_SIZE);
		sendbuf[0] = 'Y';
		send(client, sendbuf, strlen(sendbuf), 0);
		ZeroMemory(recvebuf, BUF_SIZE);
		recv(client, recvebuf, BUF_SIZE, 0);

		cout << "对出题者的查询信息如下" << endl;
		if ((recvebuf[0] == '-') && (recvebuf[1] == '>'))
		{
			cout << "无该信息对应的出题者" << endl;
		}
		else
		{
			cout << setw(PROPER_NUM) << setiosflags(ios::left) << setfill(' ') << "账号为："
				<< setw(PROPER_NUM) << setiosflags(ios::left) << setfill(' ') << "玩家名为:"
				<< setw(PROPER_NUM / 2) << setiosflags(ios::right) << setfill(' ') << "等级为:"
				<< setw(PROPER_NUM / 2) << setiosflags(ios::right) << setfill(' ') << "经验为:"
				<< setw(PROPER_NUM / 2) << setiosflags(ios::right) << setfill(' ') << "出题数:" << endl;
			int i=0 ;
			while ((recvebuf[0] != '-') || (recvebuf[1] != '>'))
			{
				if ((i % 5) < 2)
				{
					cout << setw(PROPER_NUM) << setiosflags(ios::left) << setfill(' ') << recvebuf;
				}
				else
				{
					int j = 0;
					memcpy(&j, recvebuf, 4);
					cout << setw(PROPER_NUM / 2) << setiosflags(ios::right) << setfill(' ') << j - 1;
				}
				i++;
				if ((i % 5) == 0)
					cout << endl;

				ZeroMemory(sendbuf, BUF_SIZE);
				sendbuf[0] = 'Y';
				send(client, sendbuf, strlen(sendbuf), 0);
				ZeroMemory(recvebuf, BUF_SIZE);
				recv(client, recvebuf, BUF_SIZE, 0);
			}
		}
	}
	else
	{
		cout << "服务器繁忙，请稍后再试" << endl;
		ZeroMemory(sendbuf, BUF_SIZE);
		sendbuf[0] = '*';
		send(client, sendbuf, strlen(sendbuf), 0);
	}
}

int transfer_cmd(char command)          //对命令输入进行装换，对胡乱输入具有容错性
{
	int i=0;
	switch (command)
	{
	case '1':
		i = 1;
		break;
	case '2':
		i = 2;
		break;
	case '3':
		i = 3;
		break;
	case '4':
		i = 4;
		break;
	case '5':
		i = 5;
		break;
	case '6':
		i = 6;
		break;
	case '7':
		i = 7;
		break;
	case '8':
		i = 8;
		break;
	case '9':
		i = 9;
		break;
	default:
		i = 0;
		break;
	}
	return i;
}