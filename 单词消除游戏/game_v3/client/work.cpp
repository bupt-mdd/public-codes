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

	cout << "��Դ������ ....." << endl;
	e_pool.build_pool(EASY, e_question, m_question, d_question);//����򵥵��ʵĵ��ʳ�
	m_pool.build_pool(MEDIUM, e_question, m_question, d_question);//�����еȵ��ʵĵ��ʳ�
	d_pool.build_pool(DIFFICULT, e_question, m_question, d_question);//�������ѵ��ʵĵ��ʳ�

	WSADATA			wsd;			//WSADATA����
	SOCKADDR_IN		servAddr;		//��������ַ
	char			buf[BUF_SIZE];	//�������ݻ�����
	char			bufRecv[BUF_SIZE];
	int				retVal1;			//����ֵ
	int             retVal2;
	int             retVal3;

	//��ʼ���׽��ֶ�̬��
	if (WSAStartup(MAKEWORD(2, 2), &wsd) != 0)
	{
		cout << "WSAStartup failed!" << endl;
		system("pause");
		return;
	}

	//�����׽���
	int client = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);
	int v_client1 = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);
	int v_client2 = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);
	if (INVALID_SOCKET == client || INVALID_SOCKET == v_client1 || INVALID_SOCKET == v_client2)
	{
		cout << "socket failed!" << endl;
		WSACleanup();//�ͷ��׽�����Դ
		system("pause");
		return;
	}
	//���÷�������ַ
	servAddr.sin_family = AF_INET;
	servAddr.sin_addr.s_addr = inet_addr("127.0.0.1");
	servAddr.sin_port = htons((short)4999);
	int	nServAddlen = sizeof(servAddr);
	//���ӷ�����
	retVal1 = connect(client, (LPSOCKADDR)&servAddr, sizeof(servAddr));
	retVal2 = connect(v_client1, (LPSOCKADDR)&servAddr, sizeof(servAddr));
	retVal3 = connect(v_client2, (LPSOCKADDR)&servAddr, sizeof(servAddr));
	if (SOCKET_ERROR == retVal1 || SOCKET_ERROR == retVal2 || SOCKET_ERROR == retVal3)
	{
		cout << "connect failed!" << endl;
		closesocket(client);	//�ر��׽���
		closesocket(v_client1);	//�ر��׽���
		closesocket(v_client2);	//�ر��׽���
		WSACleanup();		//�ͷ��׽�����Դ
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
		cout << "*                        ��ѡ�����                    *" << endl;
		cout << "*       1.����Ϸ           2.����            3.�˳�    *" << endl;
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
			if (1 == command)      //����Ϸģ��
			{
				listen_lab = PLAYER;
				player.gamer_operation(PLAYER, e_pool, m_pool, d_pool);
			}
			else if (2 == command)    //����ģ��
			{
				listen_lab = SET_QUE_MAN;
				set_question.adm_operation(SET_QUE_MAN, e_question, m_question, d_question, e_pool, m_pool, d_pool);
			}
			system("cls");
			cout << "********************************************************" << endl;
			cout << "*                         ��ѡ�����                   *" << endl;
			cout << "*       1.����Ϸ           2.����            3.�˳�    *" << endl;
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
			memcpy(sendbuf, &in_command, 4);   //�˳�ʱ��������������˳����󣬷���������ص�½����Ϣ���д���
			int retVal = send(player.client, sendbuf, strlen(sendbuf), 0);

			closesocket(player.client);	//�ر��׽���
			closesocket(player.v_client1);	//�ر��׽���	
			closesocket(player.v_client2);	//�ر��׽���	
			WSACleanup();			//�ͷ��׽�����Դ;

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

