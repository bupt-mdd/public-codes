#include <Winsock2.h>
#include <fstream>
#include <stdio.h>
#include <iostream>
#include <string>
#include <process.h>
#include"mylib.h"
#include"sockwork.h"
#pragma comment(lib, "ws2_32.lib")
using namespace std;

int listen_lab=TRUE;
char all_sendbuf[BUF_SIZE] = {'\0'};
int i = 0;
int main()
{
	WSADATA			wsd;			//WSADATA����
	SOCKET			sServer;		//�������׽���
	SOCKET			sClient;		//�ͻ����׽���
	SOCKET			v_sClient1;      //�ͻ����׽���
	SOCKET			v_sClient2;      //�ͻ����׽���
	SOCKADDR_IN		addrServ;;		//��������ַ
	char			recvebuf[BUF_SIZE];	//�������ݻ�����
	char			sendBuf[BUF_SIZE];//���ظ��ͻ��˵�����
	int				retVal;			//����ֵ
	//��ʼ���׽��ֶ�̬��
	if (WSAStartup(MAKEWORD(2, 2), &wsd) != 0)
	{
		cout << "WSAStartup failed!" << endl;
		system("pause");
		return 0;
	}

	//�����׽���
	sServer = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);
	if (INVALID_SOCKET == sServer)
	{
		cout << "socket failed!" << endl;
		WSACleanup();//�ͷ��׽�����Դ;
		system("pause");
		return 0;
	}
	cout << "�����������׽��ֳɹ�" << endl;
	//�������׽��ֵ�ַ 
	addrServ.sin_family = AF_INET;
	addrServ.sin_port = htons(4999);
	addrServ.sin_addr.s_addr = inet_addr("127.0.0.1");;
	//���׽���
	retVal = bind(sServer, (LPSOCKADDR)&addrServ, sizeof(SOCKADDR_IN));
	if (SOCKET_ERROR == retVal)
	{
		cout << "bind failed!" << endl;
		closesocket(sServer);	//�ر��׽���
		WSACleanup();			//�ͷ��׽�����Դ;
		system("pause");
		return 0;
	}
	cout << "�󶨶˿ڳɹ�"<<endl;

	//��ʼ���� 
	retVal = listen(sServer, 10);
	if (SOCKET_ERROR == retVal)
	{
		cout << "listen failed!" << endl;
		closesocket(sServer);	//�ر��׽���
		WSACleanup();			//�ͷ��׽�����Դ;
		system("pause");
		return 0;
	}
	cout << "��ʼ����" << endl;

	sockwork w[MAX_CLIENT];

	//���ܿͻ�������
	while (true)
	{
		sockaddr_in addrClient;
		int addrClientlen = sizeof(addrClient);
		sClient = accept(sServer, (sockaddr FAR*)&addrClient, &addrClientlen);
		v_sClient1 = accept(sServer, (sockaddr FAR*)&addrClient, &addrClientlen);
		v_sClient2 = accept(sServer, (sockaddr FAR*)&addrClient, &addrClientlen);
		cout << "���ӵ�һ���ͻ���"<<endl;

		if (INVALID_SOCKET == sClient || INVALID_SOCKET == v_sClient1||INVALID_SOCKET == v_sClient2)
		{
			cout << "accept failed!" << endl;
			closesocket(sServer);	//�ر��׽���
			WSACleanup();			//�ͷ��׽�����Դ;
			system("pause");
			return 0;
		}
		while (w[i].mysock!= -1)
		{
			i++;
			if (i >= MAX_CLIENT)
			{
				i = 0;
			}
		}          //�жϸ��˿��Ƿ�ռ�á�
		w[i].setSock(sClient, v_sClient1, v_sClient2);
		DWORD thread = i;
		HANDLE hthread = CreateThread(NULL, 0, (LPTHREAD_START_ROUTINE)run_client, &w[i], 0, &thread);
	}
	//�˳�
	closesocket(sServer);	//�ر��׽���
	closesocket(sClient);	//�ر��׽���
	WSACleanup();			//�ͷ��׽�����Դ;
	system("pause");
	system("pause");
	return 0;
}
