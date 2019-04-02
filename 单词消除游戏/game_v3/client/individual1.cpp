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

individual::individual()
	:user_experience(0), sort_standard(0), user_rank(0), que_or_passnum(0), client(0), v_client1(0), v_client2(0)
{
	ZeroMemory(user_name, PROPER_NUM);
	ZeroMemory(game_account, PROPER_NUM);
	ZeroMemory(user_password, PROPER_NUM);
}

individual::individual(char *account, char *name, char *password,
	int experience, int standard, int rank, int num, int _client, int _v_client1,int _v_client2)
	:user_experience(experience), sort_standard(standard),
	user_rank(rank), que_or_passnum(que_or_passnum), client(_client)
	, v_client1(_v_client1), v_client2(_v_client2)
{
	strcpy(game_account, account);
	strcpy(user_name, name);
	strcpy(user_password, password);
}

individual::individual(const individual& I)
	       :user_experience(I.user_experience), sort_standard(I.sort_standard),
			user_rank(I.user_rank), que_or_passnum(I.que_or_passnum), 
			client(I.client), v_client1(I.v_client1), v_client2(I.v_client2)
{
	strcpy(game_account, I.game_account);
	strcpy(user_name, I.user_name);
	strcpy(user_password, I.user_password);

}

void individual::change_username()             //可以进行注册者姓名的修改
{
	int command;
	char recvebuf[BUF_SIZE], sendbuf[BUF_SIZE] = { "\0" };
	ZeroMemory(sendbuf, BUF_SIZE);       //向服务器发送修改姓名请求
	command = CHANGE_NAME;
	memcpy(sendbuf, &command, 4);
	int retVal = send(client, sendbuf, strlen(sendbuf), 0);
	// 接收服务器端的确认，
	ZeroMemory(recvebuf, BUF_SIZE);
	recv(client, recvebuf, BUF_SIZE, 0);	

	if (recvebuf[0] == 'Y')
	{
		cout << "请输入新的用户名";
		ZeroMemory(sendbuf, BUF_SIZE);
		cin >> sendbuf;
		send(client, sendbuf, strlen(sendbuf), 0);

		ZeroMemory(recvebuf, BUF_SIZE);
		recv(client, recvebuf, BUF_SIZE, 0);		// 接收服务器端的数据，

		if (recvebuf[0] == 'Y')
		{
			ZeroMemory(user_name, PROPER_NUM);
			strcpy(user_name,sendbuf);
			cout << "姓名修改成功" << endl;
		}
		else
		{
			cout << "姓名修改失败，请稍后再试" << endl;
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

void individual::change_password()  //修改密码
{
	int command;
	char recvebuf[BUF_SIZE], sendbuf[BUF_SIZE] = { "\0" };

	ZeroMemory(sendbuf, BUF_SIZE);       //向服务器发送求
	command = CHANGE_PASSWORD;
	memcpy(sendbuf, &command, 4);
	int retVal = send(client, sendbuf, strlen(sendbuf), 0);

	// 接收服务器端的确认，
	ZeroMemory(recvebuf, BUF_SIZE);
	recv(client, recvebuf, BUF_SIZE, 0);
	if (recvebuf[0] == 'Y')
	{
		string old_password, new_password;
		cout << "请输入旧的密码";
		cin >> old_password;
		cout << "请输入新的密码";
		cin >> new_password;
		cout << "请再次输入新的密码";
		ZeroMemory(sendbuf, BUF_SIZE);
		cin >> sendbuf;
		if (new_password == sendbuf&&old_password == user_password)
		{
			send(client, sendbuf, strlen(sendbuf), 0);

			ZeroMemory(recvebuf, BUF_SIZE);
			recv(client, recvebuf, BUF_SIZE, 0);		// 接收服务器端的数据，

			if (recvebuf[0] == 'Y')
			{
				ZeroMemory(user_password, PROPER_NUM);
				strcpy(user_password, sendbuf);
				cout << "密码修改成功" << endl;
			}
			else
			{
				cout << "密码修改失败，请稍后再试" << endl;
			}
		}
		else if (new_password == sendbuf)
		{
			cout << "旧密码输入错误"<<endl;
		}
		else
			cout << "新密码两次输入不一致"<<endl;
		ZeroMemory(sendbuf, BUF_SIZE);
		sendbuf[0] = '*';
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

int individual::user_register(int role)      //玩家注册
{
	system("cls");
	int command;
	char recvebuf[BUF_SIZE], sendbuf[BUF_SIZE] = { "\0" };
	ZeroMemory(sendbuf, BUF_SIZE);       //向服务器发送请求
	command = REGISTER;
	memcpy(sendbuf, &command, 4);
	int retVal = send(client, sendbuf, strlen(sendbuf), 0);
	
	ZeroMemory(recvebuf, BUF_SIZE);
	recv(client, recvebuf, BUF_SIZE, 0);		// 接收服务器端的数据，
	if (recvebuf[0] == 'Y')
	{
	    ZeroMemory(sendbuf, BUF_SIZE);
		memcpy(sendbuf,&role,4);
		send(client, sendbuf, strlen(sendbuf), 0);
		ZeroMemory(recvebuf, BUF_SIZE);
	    recv(client, recvebuf, BUF_SIZE, 0);
		cout << "请输入注册游戏账号";
		ZeroMemory(sendbuf, BUF_SIZE);
		cin >> sendbuf;
		send(client, sendbuf, strlen(sendbuf), 0);

		ZeroMemory(recvebuf, BUF_SIZE);
		recv(client, recvebuf, BUF_SIZE, 0);		// 接收服务器端的数据，

		if (recvebuf[0] == 'Y')
		{
		cout << "请输入姓名";
		ZeroMemory(sendbuf, BUF_SIZE);
		cin >> sendbuf;
		send(client, sendbuf, strlen(sendbuf), 0);

		ZeroMemory(recvebuf, BUF_SIZE);
		recv(client, recvebuf, BUF_SIZE, 0);
			
			cout << "请输入密码";
			string code;
			cin >> code;
			cout << "请再次输入密码";
			cin >> sendbuf;
			while (code != sendbuf)
			{
				cout << "密码前后不一致，请重新输入" << endl;
				cout << "请输入密码";
				cin >> code;
				ZeroMemory(sendbuf, BUF_SIZE);
				cout << "请再次输入密码";
				cin >> sendbuf;
			}
			send(client, sendbuf, strlen(sendbuf), 0);
			ZeroMemory(recvebuf, BUF_SIZE);
			recv(client, recvebuf, BUF_SIZE, 0);

			if (recvebuf[0] == 'Y')
			{
				cout << "注册成功。" << endl;
				return TRUE;
			}
			else
			{
				cout << "注册失败";
				return FALSE;
			}
		}
		else
		{
			cout << "该账号已经存在" << endl;
			return FALSE;
		}
	}
	else
	{
		cout << "服务器繁忙" << endl;
		ZeroMemory(sendbuf, BUF_SIZE);
		sendbuf[0] = '*';
		send(client, sendbuf, strlen(sendbuf), 0);
		return FALSE;
	}	
}

int individual::user_login(int role)       //玩家登陆
{
	system("cls");
	int command;
	char recvebuf[BUF_SIZE], sendbuf[BUF_SIZE] = { "\0" };

	ZeroMemory(sendbuf, BUF_SIZE);       //向服务器发送请求
	command = LOGIN;
	memcpy(sendbuf, &command, 4);
	int retVal = send(client, sendbuf, strlen(sendbuf), 0);
	ZeroMemory(recvebuf, BUF_SIZE);
	recv(client, recvebuf, BUF_SIZE, 0);		// 接收服务器端的数据，
	if (recvebuf[0] == 'Y')
	{
		ZeroMemory(sendbuf, BUF_SIZE);
		memcpy(sendbuf,&role,4);
		send(client, sendbuf, strlen(sendbuf), 0);
		ZeroMemory(recvebuf, BUF_SIZE);
	    recv(client, recvebuf, BUF_SIZE, 0);
		//system("pause");

		cout << "请输入游戏账号";
		ZeroMemory(sendbuf, BUF_SIZE);
		cin >> sendbuf;
		send(client, sendbuf, strlen(sendbuf), 0);

		ZeroMemory(recvebuf, BUF_SIZE);
		recv(client, recvebuf, BUF_SIZE, 0);		// 接收服务器端的数据，

		if (recvebuf[0] == 'Y')
		{
			ZeroMemory(game_account, PROPER_NUM);
			strcpy(game_account, sendbuf);
			//将账号同步到本地
			cout << "请输入密码";
			ZeroMemory(sendbuf, BUF_SIZE);
			cin >> sendbuf;
			send(client, sendbuf, strlen(sendbuf), 0);
			ZeroMemory(recvebuf, BUF_SIZE);
			recv(client, recvebuf, BUF_SIZE, 0);

			if (recvebuf[0] == 'Y')
			{
				ZeroMemory(user_password, PROPER_NUM);
				strcpy(user_password, sendbuf);
				//将密码同步到本地
				ZeroMemory(sendbuf, BUF_SIZE);
				sendbuf[0] = 'Y';
				send(client, sendbuf, strlen(sendbuf), 0);
				ZeroMemory(recvebuf, BUF_SIZE);
				recv(client, recvebuf, BUF_SIZE, 0);
				ZeroMemory(user_name, PROPER_NUM);
				strcpy(user_name, recvebuf);
				//接受姓名到本地]

				memcpy(user_name, recvebuf, PROPER_NUM);
				send(client, sendbuf, strlen(sendbuf), 0);
				//cout << "labuabulabu";
				ZeroMemory(recvebuf, BUF_SIZE);
				recv(client, recvebuf, BUF_SIZE, 0);
				memcpy(&user_rank, recvebuf, 4);   //接受等级到本地
				user_rank--;

				send(client, sendbuf, strlen(sendbuf), 0);
				ZeroMemory(recvebuf, BUF_SIZE);
				recv(client, recvebuf, BUF_SIZE, 0);
				memcpy(&user_experience, recvebuf, 4);   //接受经验
				user_experience--;

				send(client, sendbuf, strlen(sendbuf), 0);
				ZeroMemory(recvebuf, BUF_SIZE);
				recv(client, recvebuf, BUF_SIZE, 0);
				memcpy(&que_or_passnum, recvebuf, 4);    //接受出题数或者闯关数
				que_or_passnum--;
				//system("pause");

				ZeroMemory(sendbuf, BUF_SIZE);
				sendbuf[0] = 'Y';
				send(client, sendbuf, strlen(sendbuf), 0);
				ZeroMemory(recvebuf, BUF_SIZE);
				recv(client, recvebuf, BUF_SIZE, 0);
				if (recvebuf[0] == 'Y')
				{
					cout << "登陆成功。" << endl;
					return TRUE;
				}
				else
				{
					cout << "此账号已经在别处登陆，请稍后再试" << endl;
					return FALSE;
				}
			}
			else
			{
				cout << "登陆失败，请检查网络状况以及账号密码等信息"<<endl;
				return FALSE;
			}
		}
		else
		{
			cout << "该账号不存在" << endl;
			return FALSE;
		}
	}
	else
	{
		cout << "服务器繁忙" << endl;
		ZeroMemory(sendbuf, BUF_SIZE);
		sendbuf[0] = '*';
		send(client, sendbuf, strlen(sendbuf), 0);
		return FALSE;
	}
}



