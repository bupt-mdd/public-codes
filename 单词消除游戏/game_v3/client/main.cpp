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

int close = FALSE;              //是否结束程序的标志，如果为TRUE则结束个线程。
int listen_lab = TRUE;          //是否监听对方挑战的监听标志
int main()
{
	work client;
	client.set_work();

	DWORD thread1 = 1;
	HANDLE hthread1 = CreateThread(NULL, 0, (LPTHREAD_START_ROUTINE)run, &client, 0, &thread1);
	   //该线程主要监听其他闯关者的挑战请求
	DWORD thread2 = 2;
	HANDLE hthread2 = CreateThread(NULL, 0, (LPTHREAD_START_ROUTINE)listen1, &client.player, 0, &thread2);
	   //该线程运行程序的注册登录以及查询等各个功能
	
	while (close==FALSE)        //当close为TRUE时，结束主线程，关闭程序。
	{
		Sleep(1);
	}
	system("cls");
	cout << "退出成功，请关闭窗口" << endl;
	system("pause");
	return 0;
}