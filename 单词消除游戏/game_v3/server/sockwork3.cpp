#include<iostream>
#include<fstream>
#include<string>
#include<iomanip>
#include<windows.h>
#include"mylib.h"
#include"sockwork.h"
using namespace std;

void sockwork::search_log()           //����ҷ�����ѯ������������󣬽��������������ͻ���
{
	int i = 0;
	int _role;
	char recvebuf[BUF_SIZE], sendbuf[BUF_SIZE] = { "\0" };
	ZeroMemory(recvebuf, BUF_SIZE);
	recv(mysock, recvebuf, BUF_SIZE, 0);
	if (recvebuf[0] != '*')
	{
		memcpy(&_role,recvebuf,4);
		ZeroMemory(sendbuf, BUF_SIZE);
		sendbuf[0] = 'Y';
		send(mysock, sendbuf, strlen(sendbuf), 0);

		char copy_account[PROPER_NUM]={'\0'},
			 copy_name[PROPER_NUM] = { '\0' };
		
		int if_log, copy_role, copy_port1, copy_port2, copy_port3;
		ifstream AccountFile1("login_score.txt");

		ZeroMemory(recvebuf, BUF_SIZE);
		recv(mysock, recvebuf, BUF_SIZE, 0);
		while (!AccountFile1.eof())
		{
			ZeroMemory(sendbuf, BUF_SIZE);
			AccountFile1 >> copy_account >> copy_name >> copy_role >> copy_port1 >> copy_port2 >>copy_port3>> if_log;
			if (AccountFile1.eof())
				break;
			if ((copy_role == _role) && (if_log == TRUE))
			{
				strcpy(sendbuf, copy_account);
				send(mysock, sendbuf, strlen(sendbuf), 0);
				ZeroMemory(recvebuf, BUF_SIZE);
				recv(mysock, recvebuf, BUF_SIZE, 0);

				ZeroMemory(sendbuf, BUF_SIZE);
				strcpy(sendbuf,copy_name);
				send(mysock, sendbuf, strlen(sendbuf), 0);
				ZeroMemory(recvebuf, BUF_SIZE);
				recv(mysock, recvebuf, BUF_SIZE, 0);
			}
		}
		AccountFile1.close();
		ZeroMemory(sendbuf, BUF_SIZE);
		sendbuf[0] = 'N';
		send(mysock, sendbuf, strlen(sendbuf), 0);
	}
}

void sockwork::challange()   //���ͻ��˷�������ս������д���
{
	char recvebuf[BUF_SIZE], recvebuf2[BUF_SIZE], sendbuf[BUF_SIZE] = { "\0" };

	ZeroMemory(recvebuf, BUF_SIZE);
	recv(mysock, recvebuf, BUF_SIZE, 0);
	char copy_account[PROPER_NUM] = { '\0' },
		 copy_name[PROPER_NUM] = { '\0' };

	int if_log, copy_role, copy_port1, copy_port2,copy_port3;
	ifstream AccountFile1("login_score.txt");
	while (!AccountFile1.eof())
	{
		AccountFile1 >> copy_account >> copy_name >> copy_role >> copy_port1 >> copy_port2 >> copy_port3>>if_log;
		if ((if_log == TRUE) && (strcmp(copy_account, recvebuf) == 0) && (copy_role == PLAYER))
			break;
	}
	//��ѯ������ս���Ƿ�����
	AccountFile1.close();
	if ((if_log == TRUE) && (strcmp(copy_account, recvebuf) == 0)&&(copy_role==PLAYER))
	{                                                   //�����ߣ������±߲���
		int command;
		command = REC_CHALLANGE;
		ZeroMemory(sendbuf, BUF_SIZE);
		memcpy(sendbuf,&command,4);
		send(copy_port2, sendbuf, strlen(sendbuf), 0);  //����ս��Ϣ��������ս��

		ZeroMemory(recvebuf, BUF_SIZE);
		recv(copy_port2, recvebuf, BUF_SIZE, 0);        //������ս����ȷ�ϡ�
		if (recvebuf[0] == 'Y')
		{

			ZeroMemory(sendbuf, BUF_SIZE);
			strcpy(sendbuf, game_account);
			send(copy_port2, sendbuf, strlen(sendbuf), 0);

			ZeroMemory(recvebuf, BUF_SIZE);
			recv(copy_port2, recvebuf, BUF_SIZE, 0);

			ZeroMemory(sendbuf, BUF_SIZE);
			strcpy(sendbuf, user_name);                
			send(copy_port2, sendbuf, strlen(sendbuf), 0);

			listen_lab = TRUE;
			DWORD thread = 1 + MAX_CLIENT;
			HANDLE hthread = CreateThread(NULL, 0, (LPTHREAD_START_ROUTINE)listen_ans, &copy_port3, 0, &thread);

			all_sendbuf[0] = 'n';
			while (1)
			{
				Sleep(3000);
				if (all_sendbuf[0] == 'n')
				{
					send(mysock, all_sendbuf, strlen(sendbuf), 0);
					ZeroMemory(recvebuf, BUF_SIZE);
					recv(mysock, recvebuf, BUF_SIZE, 0);

					if (recvebuf[0] == 'N')
					{
						listen_lab = FALSE;
						ZeroMemory(sendbuf, BUF_SIZE);
						strcpy(sendbuf, game_account);
						send(copy_port2, sendbuf, strlen(sendbuf), 0);
						break;
					}
				}
				else if (all_sendbuf[0] == 'N')
				{
					send(mysock, all_sendbuf, strlen(sendbuf), 0);
					break;
				}
				else if (all_sendbuf[0] == 'Y')
				{
					send(mysock, all_sendbuf, strlen(sendbuf), 0);
					ZeroMemory(recvebuf, BUF_SIZE);
					recv(mysock, recvebuf, BUF_SIZE, 0);//�ӷ�����ս�Ž���������ɵ���

					ZeroMemory(sendbuf, BUF_SIZE);
					strcpy(sendbuf, recvebuf);             //���õ��ʷ��͸�������ս��һ����
					send(copy_port1, sendbuf, strlen(sendbuf), 0);

					ZeroMemory(recvebuf, BUF_SIZE);
					recv(copy_port3, recvebuf, BUF_SIZE, 0);

					Sleep(WAIT_TIME * 1000);

					ZeroMemory(sendbuf, BUF_SIZE);
					sendbuf[0] = 'Y';
					send(mysock, sendbuf, strlen(sendbuf), 0);
					ZeroMemory(sendbuf, BUF_SIZE);
					sendbuf[0] = 'Y';
					send(copy_port3, sendbuf, strlen(sendbuf), 0);

					//cout << "121212" << endl;
					ZeroMemory(recvebuf, BUF_SIZE);
					recv(mysock, recvebuf, BUF_SIZE, 0);//���շ�����ս������ʱ
					//cout << "121212" << endl;
					ZeroMemory(recvebuf2, BUF_SIZE);
					recv(copy_port3, recvebuf2, BUF_SIZE, 0);//���ս�����ս������ʱ��

					if ((recvebuf[0] == 'N') && (recvebuf2[0] == 'N'))
					{
						ZeroMemory(sendbuf, BUF_SIZE);
						sendbuf[0] = 'N';
						send(mysock, sendbuf, strlen(sendbuf), 0);
						ZeroMemory(sendbuf, BUF_SIZE);
						sendbuf[0] = 'N';
						send(copy_port3, sendbuf, strlen(sendbuf), 0);
					}
					else if (recvebuf[0] == 'N')
					{
						ZeroMemory(sendbuf, BUF_SIZE);
						sendbuf[0] = 'N';
						send(mysock, sendbuf, strlen(sendbuf), 0);
						ZeroMemory(sendbuf, BUF_SIZE);
						sendbuf[0] = 'N';
						send(copy_port3, sendbuf, strlen(sendbuf), 0);
					}
					else if (recvebuf2[0] == 'N')
					{
						ZeroMemory(sendbuf, BUF_SIZE);
						sendbuf[0] = 'Y';
						send(mysock, sendbuf, strlen(sendbuf), 0);
						ZeroMemory(sendbuf, BUF_SIZE);
						sendbuf[0] = 'Y';
						send(copy_port3, sendbuf, strlen(sendbuf), 0);
					}
					else
					{//��˫����������ȷ������£���˫������ʱ������жϣ�������ս�Ƿ�ɹ�
						float time1, time2;
						memcpy(&time1, recvebuf, 4);
						memcpy(&time2, recvebuf2, 4);
						if (time1 == time2)
						{
							ZeroMemory(sendbuf, BUF_SIZE);
							sendbuf[0] = 'N';
							send(mysock, sendbuf, strlen(sendbuf), 0);

							ZeroMemory(sendbuf, BUF_SIZE);
							sendbuf[0] = 'N';
							send(copy_port3, sendbuf, strlen(sendbuf), 0);
						}
						else if (time1 < time2)
						{
							ZeroMemory(sendbuf, BUF_SIZE);
							sendbuf[0] = 'Y';
							send(mysock, sendbuf, strlen(sendbuf), 0);
							ZeroMemory(sendbuf, BUF_SIZE);
							sendbuf[0] = 'Y';
							send(copy_port3, sendbuf, strlen(sendbuf), 0);
						}
						else
						{
							ZeroMemory(sendbuf, BUF_SIZE);
							sendbuf[0] = 'N';
							send(mysock, sendbuf, strlen(sendbuf), 0);
							ZeroMemory(sendbuf, BUF_SIZE);
							sendbuf[0] = 'N';
							send(copy_port3, sendbuf, strlen(sendbuf), 0);
						}
					}
					break;
				}
			}
		}
		else if ((recvebuf[0] == 'N')&&(recvebuf[1]=='N'))
		{//������ս�������������ս������
			ZeroMemory(sendbuf, BUF_SIZE);
			sendbuf[0] = 'N';
			sendbuf[1] = 'N';
			sendbuf[2] = 'N';
			send(mysock, sendbuf, strlen(sendbuf), 0);/////////////////
		}
		else
		{//������ս���б�����������ս�����
			ZeroMemory(sendbuf, BUF_SIZE);
			sendbuf[0] = 'N';
			sendbuf[1] = 'N';
			send(mysock, sendbuf, strlen(sendbuf), 0);
		}
	}
	else
	{//����ս����ս�Ķ������ߣ��򷵻ظ���Ϣ��������ս������Ҳ�����
		ZeroMemory(sendbuf, BUF_SIZE);
		sendbuf[0] = 'N';
		sendbuf[1] = 'N';
		sendbuf[2] = 'N';
		sendbuf[3] = 'N';
		send(mysock, sendbuf, strlen(sendbuf), 0);
	}	
}
