#include <Winsock2.h>
#include<iostream>
#include<fstream>
#include<string>
#include<iomanip>
#include<windows.h>
#include"mylib.h"
#include"wordpool.h"
#include"individual.h"
#include"gamer.h"
#include"administration.h"
#include"work.h"
#pragma comment(lib,"ws2_32.lib")
using namespace std;

work::work()
{
	e_question = "\0";
	m_question = "\0";
	d_question = "\0";
}

work::~work()
{
}

void work::set_work()
{
	e_question = "easy.txt";
	m_question = "medium.txt";
	d_question = "difficult.txt";

	cout << "资源加载中 ....." << endl;
	e_pool.build_pool(EASY, e_question, m_question, d_question);//建造简单单词的单词池
	m_pool.build_pool(MEDIUM, e_question, m_question, d_question);//建造中等单词的单词池
	d_pool.build_pool(DIFFICULT, e_question, m_question, d_question);//建造困难单词的单词池

	WSADATA			wsd;			//WSADATA变量
	SOCKADDR_IN		servAddr;		//服务器地址
	char			buf[BUF_SIZE];	//接收数据缓冲区
	char			bufRecv[BUF_SIZE];
	int				retVal1;			//返回值
	int             retVal2;
	int             retVal3;

	//初始化套结字动态库
	if (WSAStartup(MAKEWORD(2, 2), &wsd) != 0)
	{
		cout << "WSAStartup failed!" << endl;
		system("pause");
		return;
	}

	//创建套接字
	int client = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);
	int v_client1 = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);
	int v_client2 = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);
	if (INVALID_SOCKET == client || INVALID_SOCKET == v_client1 || INVALID_SOCKET == v_client2)
	{
		cout << "socket failed!" << endl;
		WSACleanup();//释放套接字资源
		system("pause");
		return;
	}
	//设置服务器地址
	servAddr.sin_family = AF_INET;
	servAddr.sin_addr.s_addr = inet_addr("127.0.0.1");
	servAddr.sin_port = htons((short)4999);
	int	nServAddlen = sizeof(servAddr);
	//连接服务器
	retVal1 = connect(client, (LPSOCKADDR)&servAddr, sizeof(servAddr));
	retVal2 = connect(v_client1, (LPSOCKADDR)&servAddr, sizeof(servAddr));
	retVal3 = connect(v_client2, (LPSOCKADDR)&servAddr, sizeof(servAddr));
	if (SOCKET_ERROR == retVal1 || SOCKET_ERROR == retVal2 || SOCKET_ERROR == retVal3)
	{
		cout << "connect failed!" << endl;
		closesocket(client);	//关闭套接字
		closesocket(v_client1);	//关闭套接字
		closesocket(v_client2);	//关闭套接字
		WSACleanup();		//释放套接字资源
		close = TRUE;
		system("pause");
		return;
	}
	player.client = client;
	set_question.client = client;

	player.v_client1 = v_client1;
	set_question.v_client1 = v_client1;

	player.v_client2 = v_client2;
	set_question.v_client2 = v_client2;

}

void work::run_client()
{
	while (true)
	{
		system("cls");
		cout << "********************************************************" << endl;
		cout << "*                        请选择操作                    *" << endl;
		cout << "*       1.玩游戏           2.出题            3.退出    *" << endl;
		cout << "*                                                      *" << endl;
		cout << "********************************************************" << endl;
		int command;
		char cmd_str[MAX_ARRAY_NUM];
		char cmd;
		cin >> cmd_str;
		cmd = cmd_str[0];
		command = transfer_cmd(cmd);
		char recvebuf[20];
		while (command != 3)
		{
			if (1 == command)      //玩游戏模块
			{
				listen_lab = PLAYER;
				player.gamer_operation(PLAYER, e_pool, m_pool, d_pool);
			}
			else if (2 == command)    //出题模块
			{
				listen_lab = SET_QUE_MAN;
				set_question.adm_operation(SET_QUE_MAN, e_question, m_question, d_question, e_pool, m_pool, d_pool);
			}
			system("cls");
			cout << "********************************************************" << endl;
			cout << "*                         请选择操作                   *" << endl;
			cout << "*       1.玩游戏           2.出题            3.退出    *" << endl;
			cout << "*                                                      *" << endl;
			cout << "********************************************************" << endl;
			cin >> cmd_str;
			cmd = cmd_str[0];
			command = transfer_cmd(cmd);
		}
		if (command == 3)
		{
			int in_command;
			char sendbuf[BUF_SIZE] = { "\0" };
			ZeroMemory(sendbuf, BUF_SIZE);
			in_command = END_BACK;
			memcpy(sendbuf, &in_command, 4);   //退出时，向服务器发送退出请求，服务器对相关登陆者信息进行处理
			int retVal = send(player.client, sendbuf, strlen(sendbuf), 0);

			closesocket(player.client);	//关闭套接字
			closesocket(player.v_client1);	//关闭套接字	
			closesocket(player.v_client2);	//关闭套接字	
			WSACleanup();			//释放套接字资源;

			close = TRUE;
			return;
		}
		
	}
}

void listen1(void* lpParameter)
{
	gamer *_individual = (gamer*)lpParameter;

		_individual->listen();
		return;

}

void run(void* lpParameter)
{
	work *_client = (work*)lpParameter;

	_client->run_client();
	return;
}

