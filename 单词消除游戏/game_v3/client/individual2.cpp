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

void individual::merge(individual *&Arrayptr, individual *&Arrayptr_copy, int left, int q, int right)
{
	int n = right - left + 1, i, j, num;
	int num1 = q - left + 1;
	int num2 = right - q;
	for (i = 0, j = 0, num = 0; (i<num1) && (j<num2); num++)
	{
		if (Arrayptr[left + i].sort_standard > Arrayptr[q + 1 + j].sort_standard)
		{
			Arrayptr_copy[left + num] = Arrayptr[left + i];
			i++;
		}
		else
		{
			Arrayptr_copy[left + num] = Arrayptr[q + 1 + j];
			j++;
		}
	}
	if (i == num1)
		for (; j<num2; j++, num++)
			Arrayptr_copy[left + num] = Arrayptr[q + 1 + j];
	else
		for (; i<num1; i++, num++)
			Arrayptr_copy[left + num] = Arrayptr[left + i];
}

void individual::merge_pass(individual *&Arrayptr, individual *&Arrayptr_1, int s, int num)
{
	int i = 0;
	while ((i + 2 * s) <= num)               //（i+2*s-1）<num 
	{
		merge(Arrayptr, Arrayptr_1, i, i + s - 1, i + 2 * s - 1);
		i = i + (2 * s);
	}
	if (i + s<num)
		merge(Arrayptr, Arrayptr_1, i, i + s - 1, num - 1);
	else
		for (int j = i; j <= num - 1; j++)
			Arrayptr_1[j] = Arrayptr[j];
}

void individual::merge_sort(individual *&Arrayptr, int num)
{
	individual *Arrayptr_1 = new individual[num];
	int s = 1;
	while (s<num)
	{
		merge_pass(Arrayptr, Arrayptr_1, s, num);
		s += s;
		merge_pass(Arrayptr_1, Arrayptr, s, num);
		s += s;
	}
	delete[] Arrayptr_1;
}

//以上三个为非递归形式的合并排序算法。
//可以实现对玩家信息按照相关属性进行从大到小排序。

void individual::show_result(individual *Arrayptr, int num)
{
	cout << setw(PROPER_NUM / 4) << setiosflags(ios::left) << setfill(' ') << "名次："
		<< setw(PROPER_NUM) << setiosflags(ios::left) << setfill(' ') << "账号为："
		<< setw(PROPER_NUM) << setiosflags(ios::left) << setfill(' ') << "玩家名为:"
		<< setw(PROPER_NUM / 2) << setiosflags(ios::left) << setfill(' ') << "等级为:"
		<< setw(PROPER_NUM / 2) << setiosflags(ios::left) << setfill(' ') << "经验为:"
		<< setw(PROPER_NUM / 2) << setiosflags(ios::left) << setfill(' ') << "闯关数:" << endl;
	for (int i = 0; i < num; i++)
	{
		cout << setw(PROPER_NUM / 4) << setiosflags(ios::left) << setfill(' ') << i + 1  
			<< setw(PROPER_NUM) << setiosflags(ios::left) << setfill(' ') << Arrayptr[i].game_account
			<< setw(PROPER_NUM) << setiosflags(ios::left) << setfill(' ') << Arrayptr[i].user_name
			<< setw(PROPER_NUM / 2) << setiosflags(ios::left) << setfill(' ') << Arrayptr[i].user_rank
			<< setw(PROPER_NUM / 2) << setiosflags(ios::left) << setfill(' ') << Arrayptr[i].user_experience
			<< setw(PROPER_NUM / 2) << setiosflags(ios::left) << setfill(' ') << Arrayptr[i].que_or_passnum << endl;
	}
}

//对排序的结果进行输出

void individual::sort()
{
	individual *Arrayptr = new individual[MAX_ARRAY_NUM];
	int command;
	char recvebuf[BUF_SIZE], sendbuf[BUF_SIZE] = { "\0" };

	ZeroMemory(sendbuf, BUF_SIZE);       //向服务器发送请求
	command = SORT;
	memcpy(sendbuf, &command, 4);
	send(client, sendbuf, strlen(sendbuf), 0);

	ZeroMemory(recvebuf, BUF_SIZE);
	recv(client, recvebuf, BUF_SIZE, 0);
	if (recvebuf[0] == 'Y')
	{
		int out_command;
		system("cls");
		cout << "********************************************************" << endl;
		cout << "*                   请选择排序对象                     *" << endl;
		cout << "*         " << PLAYER << "玩家          " << SET_MAN << "出题者        3退出　        *" << endl;
		cout << "********************************************************" << endl;
		ZeroMemory(sendbuf, BUF_SIZE);       //向服务器发送请求
		char cmd_str[MAX_ARRAY_NUM];
		char cmd;
		cin >> cmd_str;
		cmd = cmd_str[0];
		out_command = transfer_cmd(cmd);
		
		while (out_command != 3)
		{
			if ((out_command == SET_QUE_MAN) || (out_command == PLAYER))//通过与服务器联系，把玩家信息接收到客户端，
			{                                                     //然后调用排序算法进行排序输出
				memcpy(sendbuf, &out_command, 4);
				send(client, sendbuf, strlen(sendbuf), 0);
				ZeroMemory(recvebuf, BUF_SIZE);
				recv(client, recvebuf, BUF_SIZE, 0);
				if (recvebuf[0] == 'Y')
				{
					int i = 0;
					while (true)
					{
						ZeroMemory(sendbuf, BUF_SIZE);
						sendbuf[0] = 'Y';
						send(client, sendbuf, strlen(sendbuf), 0);
						ZeroMemory(recvebuf, BUF_SIZE);
						recv(client, recvebuf, BUF_SIZE, 0);
						if (recvebuf[0] == '*')
							break;
						ZeroMemory(Arrayptr[i].game_account, PROPER_NUM);
						strcpy(Arrayptr[i].game_account, recvebuf);

						sendbuf[0] = 'Y';
						send(client, sendbuf, strlen(sendbuf), 0);
						ZeroMemory(recvebuf, BUF_SIZE);
						recv(client, recvebuf, BUF_SIZE, 0);
						ZeroMemory(Arrayptr[i].user_name, PROPER_NUM);
						strcpy(Arrayptr[i].user_name, recvebuf);

						sendbuf[0] = 'Y';
						send(client, sendbuf, strlen(sendbuf), 0);
						ZeroMemory(recvebuf, BUF_SIZE);
						recv(client, recvebuf, BUF_SIZE, 0);
						memcpy(&Arrayptr[i].user_rank, recvebuf, 4);
						Arrayptr[i].user_rank--;

						sendbuf[0] = 'Y';
						send(client, sendbuf, strlen(sendbuf), 0);
						ZeroMemory(recvebuf, BUF_SIZE);
						recv(client, recvebuf, BUF_SIZE, 0);
						memcpy(&Arrayptr[i].user_experience, recvebuf, 4);
						Arrayptr[i].user_experience--;

						sendbuf[0] = 'Y';
						send(client, sendbuf, strlen(sendbuf), 0);
						ZeroMemory(recvebuf, BUF_SIZE);
						recv(client, recvebuf, BUF_SIZE, 0);
						memcpy(&Arrayptr[i].que_or_passnum, recvebuf, 4);
						Arrayptr[i].que_or_passnum--;
						i++;
					}

					int num = i;
					int in_command;
					system("cls");
					cout << "********************************************************" << endl;
					cout << "*                   请选择排序操作                     *" << endl;
					cout << "*         1按等级                 2按出题数（过关数）  *" << endl;
					cout << "*         3按经验                 4退出                *" << endl;
					cout << "********************************************************" << endl;
					cin >> cmd_str;
					cmd = cmd_str[0];
					in_command = transfer_cmd(cmd);
					
					system("cls");
					while (in_command != 4 && out_command != 3)
					{
						switch (in_command)
						{
						case 1:
							for (int i = 0; i < num; i++)
							{
								Arrayptr[i].sort_standard = Arrayptr[i].user_rank;
							}
							merge_sort(Arrayptr, num);
							system("cls");
							show_result(Arrayptr, num);
							break;
						case 2:
							for (int i = 0; i < num; i++)
							{
								Arrayptr[i].sort_standard = Arrayptr[i].que_or_passnum;
							}
							merge_sort(Arrayptr, num);
							system("cls");
							show_result(Arrayptr, num);
							break;
						case 3:
							for (int i = 0; i < num; i++)
							{
								Arrayptr[i].sort_standard = Arrayptr[i].user_experience;
							}
							merge_sort(Arrayptr, num);
							system("cls");
							show_result(Arrayptr, num);
							break;
						default:break;
						}
						cout << "********************************************************" << endl;
						cout << "*                   请选择排序操作                     *" << endl;
						cout << "*         1按等级                 2按出题数（过关数）  *" << endl;
						cout << "*         3按经验                 4退出                *" << endl;
						cout << "********************************************************" << endl;
						cin >> cmd_str;
						cmd = cmd_str[0];
						in_command = transfer_cmd(cmd);

						system("cls");
					}
				}
			}
			system("cls");
			cout << "********************************************************" << endl;
			cout << "*                   请选择排序对象                     *" << endl;
			cout << "*         " << PLAYER << "玩家          " << SET_MAN << "出题者        3退出　        *" << endl;
			cout << "********************************************************" << endl;
			ZeroMemory(sendbuf, BUF_SIZE);       //向服务器发送请求
			cin >> cmd_str;
			cmd = cmd_str[0];
			out_command = transfer_cmd(cmd);

			system("cls");
		}
		out_command = 3;
		memcpy(sendbuf, &out_command, 4);
		send(client, sendbuf, strlen(sendbuf), 0);
		
	}
	else
	{
		cout << "服务器繁忙，请稍后再试" << endl;
		ZeroMemory(sendbuf, BUF_SIZE);
		sendbuf[0] = '*';
		send(client, sendbuf, strlen(sendbuf), 0);
	}
}

void individual::search_log()   //实现当前登陆者的信息查询
{
	int command;
	char cmd_str[MAX_ARRAY_NUM];
	char cmd;
	system("cls");
	cout << "********************************************************" << endl;
	cout << "*                    请选择操作                        *" << endl;
	cout << "*    " << PLAYER << "查询闯关者      " << SET_QUE_MAN << "查询出题者         3退出        *" << endl;
	cout << "********************************************************" << endl;
	cin >> cmd_str;
	cmd = cmd_str[0];
	command = transfer_cmd(cmd);
	while (command!=3)
	{
		if (command == PLAYER)
		{
			insearch_logon(PLAYER);
		}
		else
		{
			insearch_logon(SET_QUE_MAN);
		}
		cout << "********************************************************" << endl;
		cout << "*                    请选择操作                        *" << endl;
		cout << "*    "<<PLAYER<<"查询闯关者      "<<SET_QUE_MAN<<"查询出题者         3退出        *" << endl;
		cout << "********************************************************" << endl;
		cin >> cmd_str;
		cmd = cmd_str[0];
		command = transfer_cmd(cmd);
	}
}

void individual::insearch_logon(int _role)   //可分别对闯关者和出题者进行查询
{
	system("cls");
	int command;
	char recvebuf[BUF_SIZE], sendbuf[BUF_SIZE] = { "\0" };

	ZeroMemory(sendbuf, BUF_SIZE);       //向服务器发送请求
	command = SEARCH_LOG;
	memcpy(sendbuf, &command, 4);
	send(client, sendbuf, strlen(sendbuf), 0);

	ZeroMemory(recvebuf, BUF_SIZE);
	recv(client, recvebuf, BUF_SIZE, 0);
	//cout << recvebuf<< endl;///////////////
	if (recvebuf[0] == 'Y')
	{
		ZeroMemory(sendbuf, BUF_SIZE);       //传输查询对象。
		memcpy(sendbuf, &_role, 4);
		send(client, sendbuf, strlen(sendbuf), 0);

		ZeroMemory(recvebuf, BUF_SIZE);//接收确认。
		recv(client, recvebuf, BUF_SIZE, 0);
		cout << "当前登陆者信息" << endl;

		cout << setw(PROPER_NUM) << setiosflags(ios::left) << setfill(' ') << "序号为："
			<< setw(PROPER_NUM) << setiosflags(ios::left) << setfill(' ') << "账号为："
			 << setw(PROPER_NUM) << setiosflags(ios::left) << setfill(' ') << "玩家名为:"<< endl;
		int i = 0;
		ZeroMemory(sendbuf, BUF_SIZE);
		sendbuf[0] = 'Y';
		send(client, sendbuf, strlen(sendbuf), 0);//告诉发送方可以发数据
		ZeroMemory(recvebuf, BUF_SIZE);
		recv(client, recvebuf, BUF_SIZE, 0);//接收确认。

		while (recvebuf[0] != 'N')
		{
			if (i%2==0)
				cout << setw(PROPER_NUM) << setiosflags(ios::left) << setfill(' ') << i / 2 + 1;
			if ((i % 2) < 2)
			{
				cout << setw(PROPER_NUM) << setiosflags(ios::left) << setfill(' ') << recvebuf;
			}
			i++;
			if ((i % 2) == 0)
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


void individual::operate(int role)    //查询与属性修改的相关模块
{
	int command;
	system("cls");
	cout << "********************************************************" << endl;
	cout << "*                    请选择操作                        *" << endl;
	cout << "*    1查询所有成员     2按属性查询      3修改密码      *" << endl;
	cout << "*    4修改姓名                          5排序输出      *" << endl;
	cout << "*    6查询已登陆者                      7退出          *" << endl;
	cout << "********************************************************" << endl;
	char cmd_str[MAX_ARRAY_NUM];
	char cmd;
	cin >> cmd_str;
	cmd = cmd_str[0];
	command = transfer_cmd(cmd);
	
	while (command != 7)
	{
		system("cls");
		switch (command)
		{
		case 1:
			search_All_individual();
			break;
		case 2:
			search_individual();
			break;
		case 3:
			system("cls");
			change_password();
			break;
		case 4:
			change_username();
			break;
		case 5:
			sort();
				break;
		case 6:
			search_log();
			break;
		default:break;
		}
		cout << "********************************************************" << endl;
		cout << "*                    请选择操作                        *" << endl;
		cout << "*    1查询所有成员     2按属性查询      3修改密码      *" << endl;
		cout << "*    4修改姓名                          5排序输出      *" << endl;
		cout << "*    6查询已登陆者                      7退出          *" << endl;
		cout << "********************************************************" << endl;
		cin >> cmd_str;
		cmd = cmd_str[0];
		command = transfer_cmd(cmd);
	}

}

int individual::init_operate(int command, int role)
{
	if (REGISTER != command)
		return user_login(role);
	else
		return user_register(role);
}

