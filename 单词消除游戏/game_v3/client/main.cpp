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

int close = FALSE;              //�Ƿ��������ı�־�����ΪTRUE��������̡߳�
int listen_lab = TRUE;          //�Ƿ�����Է���ս�ļ�����־
int main()
{
	work client;
	client.set_work();

	DWORD thread1 = 1;
	HANDLE hthread1 = CreateThread(NULL, 0, (LPTHREAD_START_ROUTINE)run, &client, 0, &thread1);
	   //���߳���Ҫ�������������ߵ���ս����
	DWORD thread2 = 2;
	HANDLE hthread2 = CreateThread(NULL, 0, (LPTHREAD_START_ROUTINE)listen1, &client.player, 0, &thread2);
	   //���߳����г����ע���¼�Լ���ѯ�ȸ�������
	
	while (close==FALSE)        //��closeΪTRUEʱ���������̣߳��رճ���
	{
		Sleep(1);
	}
	system("cls");
	cout << "�˳��ɹ�����رմ���" << endl;
	system("pause");
	return 0;
}