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
	WSADATA			wsd;			//WSADATA变量
	SOCKET			sServer;		//服务器套接字
	SOCKET			sClient;		//客户端套接字
	SOCKET			v_sClient1;      //客户端套接字
	SOCKET			v_sClient2;      //客户端套接字
	SOCKADDR_IN		addrServ;;		//服务器地址
	char			recvebuf[BUF_SIZE];	//接收数据缓冲区
	char			sendBuf[BUF_SIZE];//返回给客户端得数据
	int				retVal;			//返回值
	//初始化套结字动态库
	if (WSAStartup(MAKEWORD(2, 2), &wsd) != 0)
	{
		cout << "WSAStartup failed!" << endl;
		system("pause");
		return 0;
	}

	//创建套接字
	sServer = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);
	if (INVALID_SOCKET == sServer)
	{
		cout << "socket failed!" << endl;
		WSACleanup();//释放套接字资源;
		system("pause");
		return 0;
	}
	cout << "创建服务器套接字成功" << endl;
	//服务器套接字地址 
	addrServ.sin_family = AF_INET;
	addrServ.sin_port = htons(4999);
	addrServ.sin_addr.s_addr = inet_addr("127.0.0.1");;
	//绑定套接字
	retVal = bind(sServer, (LPSOCKADDR)&addrServ, sizeof(SOCKADDR_IN));
	if (SOCKET_ERROR == retVal)
	{
		cout << "bind failed!" << endl;
		closesocket(sServer);	//关闭套接字
		WSACleanup();			//释放套接字资源;
		system("pause");
		return 0;
	}
	cout << "绑定端口成功"<<endl;

	//开始监听 
	retVal = listen(sServer, 10);
	if (SOCKET_ERROR == retVal)
	{
		cout << "listen failed!" << endl;
		closesocket(sServer);	//关闭套接字
		WSACleanup();			//释放套接字资源;
		system("pause");
		return 0;
	}
	cout << "开始监听" << endl;

	sockwork w[MAX_CLIENT];

	//接受客户端请求
	while (true)
	{
		sockaddr_in addrClient;
		int addrClientlen = sizeof(addrClient);
		sClient = accept(sServer, (sockaddr FAR*)&addrClient, &addrClientlen);
		v_sClient1 = accept(sServer, (sockaddr FAR*)&addrClient, &addrClientlen);
		v_sClient2 = accept(sServer, (sockaddr FAR*)&addrClient, &addrClientlen);
		cout << "连接到一个客户端"<<endl;

		if (INVALID_SOCKET == sClient || INVALID_SOCKET == v_sClient1||INVALID_SOCKET == v_sClient2)
		{
			cout << "accept failed!" << endl;
			closesocket(sServer);	//关闭套接字
			WSACleanup();			//释放套接字资源;
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
		}          //判断给端口是否被占用。
		w[i].setSock(sClient, v_sClient1, v_sClient2);
		DWORD thread = i;
		HANDLE hthread = CreateThread(NULL, 0, (LPTHREAD_START_ROUTINE)run_client, &w[i], 0, &thread);
	}
	//退出
	closesocket(sServer);	//关闭套接字
	closesocket(sClient);	//关闭套接字
	WSACleanup();			//释放套接字资源;
	system("pause");
	system("pause");
	return 0;
}
