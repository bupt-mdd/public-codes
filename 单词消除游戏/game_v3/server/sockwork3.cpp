#include<iostream>
#include<fstream>
#include<string>
#include<iomanip>
#include<windows.h>
#include"mylib.h"
#include"sockwork.h"
using namespace std;

void sockwork::search_log()           //当玩家发出查询在线人数命令后，将在线人数发给客户端
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

void sockwork::challange()   //将客户端发出的挑战请求进行处理。
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
	//查询请求挑战者是否在线
	AccountFile1.close();
	if ((if_log == TRUE) && (strcmp(copy_account, recvebuf) == 0)&&(copy_role==PLAYER))
	{                                                   //若在线，进行下边操作
		int command;
		command = REC_CHALLANGE;
		ZeroMemory(sendbuf, BUF_SIZE);
		memcpy(sendbuf,&command,4);
		send(copy_port2, sendbuf, strlen(sendbuf), 0);  //把挑战信息发给被挑战者

		ZeroMemory(recvebuf, BUF_SIZE);
		recv(copy_port2, recvebuf, BUF_SIZE, 0);        //接收挑战方的确认。
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
					recv(mysock, recvebuf, BUF_SIZE, 0);//从发起挑战放接收随机生成单词

					ZeroMemory(sendbuf, BUF_SIZE);
					strcpy(sendbuf, recvebuf);             //将该单词发送给接收挑战的一方。
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
					recv(mysock, recvebuf, BUF_SIZE, 0);//接收发起挑战方的用时
					//cout << "121212" << endl;
					ZeroMemory(recvebuf2, BUF_SIZE);
					recv(copy_port3, recvebuf2, BUF_SIZE, 0);//接收接受挑战方的用时间

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
					{//当双方都输入正确的情况下，对双方所用时间进行判断，决定挑战是否成功
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
		{//告诉挑战方该玩家正在挑战别的玩家
			ZeroMemory(sendbuf, BUF_SIZE);
			sendbuf[0] = 'N';
			sendbuf[1] = 'N';
			sendbuf[2] = 'N';
			send(mysock, sendbuf, strlen(sendbuf), 0);/////////////////
		}
		else
		{//告诉挑战方有别的玩家正在挑战该玩家
			ZeroMemory(sendbuf, BUF_SIZE);
			sendbuf[0] = 'N';
			sendbuf[1] = 'N';
			send(mysock, sendbuf, strlen(sendbuf), 0);
		}
	}
	else
	{//若挑战方挑战的对象不在线，则返回该信息，告诉挑战方该玩家不在线
		ZeroMemory(sendbuf, BUF_SIZE);
		sendbuf[0] = 'N';
		sendbuf[1] = 'N';
		sendbuf[2] = 'N';
		sendbuf[3] = 'N';
		send(mysock, sendbuf, strlen(sendbuf), 0);
	}	
}
