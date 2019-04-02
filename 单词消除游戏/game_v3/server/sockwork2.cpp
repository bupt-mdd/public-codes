#include<iostream>
#include<fstream>
#include<string>
#include<iomanip>
#include<windows.h>
#include"mylib.h"
#include"sockwork.h"
using namespace std;

void sockwork::search_All_individual()//查询所用玩家的信息，并传送给客户端
{
	int i = 0;
	char recvebuf[BUF_SIZE], sendbuf[BUF_SIZE] = { "\0" };
	ZeroMemory(recvebuf, BUF_SIZE);
	recv(mysock, recvebuf, BUF_SIZE, 0);
	if (recvebuf[0] != '*')
	{
		int copy_rank, copy_experience, copy_num;
		ifstream AccountFile1("player_information.txt");

		while (!AccountFile1.eof())
		{
			ZeroMemory(sendbuf, BUF_SIZE);
			AccountFile1 >> sendbuf;
			send(mysock, sendbuf, strlen(sendbuf), 0);
			ZeroMemory(recvebuf, BUF_SIZE);
			recv(mysock, recvebuf, BUF_SIZE, 0);
			
			ZeroMemory(sendbuf, BUF_SIZE);
			AccountFile1 >> sendbuf;
			send(mysock, sendbuf, strlen(sendbuf), 0);
			ZeroMemory(recvebuf, BUF_SIZE);
			recv(mysock, recvebuf, BUF_SIZE, 0);
			
			AccountFile1 >> sendbuf;
			ZeroMemory(sendbuf, BUF_SIZE);
			AccountFile1 >> i;
			i++;
			memcpy(sendbuf, &i, 4);
			send(mysock, sendbuf, strlen(sendbuf), 0);
			ZeroMemory(recvebuf, BUF_SIZE);
			recv(mysock, recvebuf, BUF_SIZE, 0);
			
			ZeroMemory(sendbuf, BUF_SIZE);
			AccountFile1 >> i;
			i++;
			memcpy(sendbuf, &i, 4);
			send(mysock, sendbuf, strlen(sendbuf), 0);
			ZeroMemory(recvebuf, BUF_SIZE);
			recv(mysock, recvebuf, BUF_SIZE, 0);
			
			ZeroMemory(sendbuf, BUF_SIZE);
			AccountFile1 >> i;
			i++;
			memcpy(sendbuf, &i, 4);
			send(mysock, sendbuf, strlen(sendbuf), 0);
			ZeroMemory(recvebuf, BUF_SIZE);
			recv(mysock, recvebuf, BUF_SIZE, 0);
			
		}
		AccountFile1.close();
		ZeroMemory(sendbuf, BUF_SIZE);
		sendbuf[0] = 'N';
		send(mysock, sendbuf, strlen(sendbuf), 0);
		ZeroMemory(recvebuf, BUF_SIZE);
		recv(mysock, recvebuf, BUF_SIZE, 0);

		ZeroMemory(sendbuf, BUF_SIZE);
		sendbuf[0] = 'Y';
		send(mysock, sendbuf, strlen(sendbuf), 0);
		ZeroMemory(recvebuf, BUF_SIZE);
		recv(mysock, recvebuf, BUF_SIZE, 0);

		ifstream AccountFile2("adm_information.txt");
		while (!AccountFile2.eof())
		{
			ZeroMemory(sendbuf, BUF_SIZE);
			AccountFile2 >> sendbuf;
			send(mysock, sendbuf, strlen(sendbuf), 0);
			ZeroMemory(recvebuf, BUF_SIZE);
			recv(mysock, recvebuf, BUF_SIZE, 0);

			ZeroMemory(sendbuf, BUF_SIZE);
			AccountFile2 >> sendbuf;
			send(mysock, sendbuf, strlen(sendbuf), 0);
			ZeroMemory(recvebuf, BUF_SIZE);
			recv(mysock, recvebuf, BUF_SIZE, 0);

			AccountFile2 >> sendbuf;
			ZeroMemory(sendbuf, BUF_SIZE);
			AccountFile2 >> i;
			i++;
			memcpy(sendbuf, &i, 4);
			send(mysock, sendbuf, strlen(sendbuf), 0);
			ZeroMemory(recvebuf, BUF_SIZE);
			recv(mysock, recvebuf, BUF_SIZE, 0);

			ZeroMemory(sendbuf, BUF_SIZE);
			AccountFile2 >> i;
			i++;
			memcpy(sendbuf, &i, 4);
			send(mysock, sendbuf, strlen(sendbuf), 0);
			ZeroMemory(recvebuf, BUF_SIZE);
			recv(mysock, recvebuf, BUF_SIZE, 0);

			ZeroMemory(sendbuf, BUF_SIZE);
			AccountFile2 >> i;
			i++;
			memcpy(sendbuf, &i, 4);
			send(mysock, sendbuf, strlen(sendbuf), 0);
			ZeroMemory(recvebuf, BUF_SIZE);
			recv(mysock, recvebuf, BUF_SIZE, 0);
	
		}
		AccountFile2.close();
		ZeroMemory(sendbuf, BUF_SIZE);
		sendbuf[0] = 'N';
		send(mysock, sendbuf, strlen(sendbuf), 0);
	}
}

void sockwork::sort()//接收到排序请求后。将所有玩家信息发送给客户端
{
	char recvebuf[BUF_SIZE], sendbuf[BUF_SIZE] = { "\0" };
	int command = 0;
	string cur_inf;
	ZeroMemory(recvebuf, BUF_SIZE);
	recv(mysock, recvebuf, BUF_SIZE, 0);
	if (recvebuf[0] != '*')
	{
		memcpy(&command, recvebuf, 4);
		cout << command;
		while (command != 3)
		{
			if ((command == PLAYER) || (command == SET_QUE_MAN))
			{
				if (command == SET_QUE_MAN)
				{
					cur_inf = "adm_information.txt";
				}
				else
					cur_inf = "player_information.txt";

				ifstream AccountFile1(cur_inf);
				ZeroMemory(sendbuf, BUF_SIZE);
				sendbuf[0] = 'Y';
				send(mysock, sendbuf, strlen(sendbuf), 0);
				ZeroMemory(recvebuf, BUF_SIZE);
				recv(mysock, recvebuf, BUF_SIZE, 0);
				int i = 0;
				while (!AccountFile1.eof())
				{
			
					ZeroMemory(sendbuf, BUF_SIZE);
					AccountFile1 >> sendbuf;
					send(mysock, sendbuf, strlen(sendbuf), 0);
					ZeroMemory(recvebuf, BUF_SIZE);
					recv(mysock, recvebuf, BUF_SIZE, 0);
					
					ZeroMemory(sendbuf, BUF_SIZE);
					AccountFile1 >> sendbuf;
					send(mysock, sendbuf, strlen(sendbuf), 0);
					ZeroMemory(recvebuf, BUF_SIZE);
					recv(mysock, recvebuf, BUF_SIZE, 0);
					
					AccountFile1 >> sendbuf;
					ZeroMemory(sendbuf, BUF_SIZE);
					AccountFile1 >> i;
					i++;
					memcpy(sendbuf, &i, 4);
					send(mysock, sendbuf, strlen(sendbuf), 0);
					ZeroMemory(recvebuf, BUF_SIZE);
					recv(mysock, recvebuf, BUF_SIZE, 0);
					
					ZeroMemory(sendbuf, BUF_SIZE);
					AccountFile1 >> i;
					i++;
					memcpy(sendbuf, &i, 4);
					send(mysock, sendbuf, strlen(sendbuf), 0);
					ZeroMemory(recvebuf, BUF_SIZE);
					recv(mysock, recvebuf, BUF_SIZE, 0);
					
					ZeroMemory(sendbuf, BUF_SIZE);
					AccountFile1 >> i;
					i++;
					memcpy(sendbuf, &i, 4);
					send(mysock, sendbuf, strlen(sendbuf), 0);
					ZeroMemory(recvebuf, BUF_SIZE);
					recv(mysock, recvebuf, BUF_SIZE, 0);
					

				}
				ZeroMemory(sendbuf, BUF_SIZE);
				sendbuf[0] = '*';
				send(mysock, sendbuf, strlen(sendbuf), 0);
				AccountFile1.close();

				ZeroMemory(recvebuf, BUF_SIZE);
				recv(mysock, recvebuf, BUF_SIZE, 0);
				memcpy(&command, recvebuf, 4);
			}
		}

	}
}

void sockwork::change()     //接收到修改请求后，对玩家的经验等进行修改。
{
	char recvebuf[BUF_SIZE], sendbuf[BUF_SIZE] = { "\0" };

	ZeroMemory(recvebuf, BUF_SIZE);
	recv(mysock, recvebuf, BUF_SIZE, 0);
	int _role;
	if (recvebuf[0] != '*')
	{
		memcpy(&_role, recvebuf, 4);
		if (_role == SET_QUE_MAN)
		{
			char copy_account[PROPER_NUM] = {"\0"},
				 copy_name[PROPER_NUM] = {"\0"},
				 copy_code[PROPER_NUM] = {"\0"};

			int copy_rank, copy_experience, copy_num;
			fstream AccountFile("adm_information.txt", ios::in | ios::out);
			AccountFile.seekg(ios::beg);
			AccountFile >> copy_account;
			while (!AccountFile.eof() && (strcmp(copy_account , game_account)!=0))
			{
				AccountFile >> copy_name
					>> copy_code
					>> copy_rank
					>> copy_experience
					>> copy_num;
				AccountFile >> copy_account;
			}
			ZeroMemory(sendbuf, BUF_SIZE);
			sendbuf[0] = 'Y';
			send(mysock, sendbuf, strlen(sendbuf), 0);
			
			ZeroMemory(recvebuf, BUF_SIZE);
			recv(mysock, recvebuf, BUF_SIZE, 0);
			memcpy(&que_or_passnum, recvebuf, 4);
			que_or_passnum--;
			ZeroMemory(sendbuf, BUF_SIZE);
			sendbuf[0] = 'Y';
			send(mysock, sendbuf, strlen(sendbuf), 0);

			int cur_experience;
			ZeroMemory(recvebuf, BUF_SIZE);
			recv(mysock, recvebuf, BUF_SIZE, 0);
			memcpy(&cur_experience, recvebuf, 4);
			cur_experience--;
			ZeroMemory(sendbuf, BUF_SIZE);
			sendbuf[0] = 'Y';
			send(mysock, sendbuf, strlen(sendbuf), 0);

			user_experience = user_experience + cur_experience;

			if (user_experience >= ((user_rank + 1)*INC_RANK_RATIO))
			{
				user_experience = user_experience - ((user_rank + 1)*INC_RANK_RATIO);
				user_rank++;
			}

			streampos position = AccountFile.tellg();
			AccountFile.seekp(position);
			AccountFile << " " << setw(PROPER_NUM) << setiosflags(ios::right) << setfill(' ') << user_name
				<< " " << setw(PROPER_NUM) << setiosflags(ios::right) << setfill(' ') << user_password
				<< " " << setw(PROPER_NUM) << setiosflags(ios::right) << setfill(' ') << user_rank
				<< " " << setw(PROPER_NUM) << setiosflags(ios::right) << setfill(' ') << user_experience
				<< " " << setw(PROPER_NUM) << setiosflags(ios::right) << setfill(' ') << que_or_passnum;
			AccountFile.close();
		}
		else
		{
			char copy_account[PROPER_NUM] = { "\0" },
				copy_name[PROPER_NUM] = { "\0" },
				copy_code[PROPER_NUM] = { "\0" };

			int copy_rank, copy_experience, copy_num;
			fstream AccountFile("player_information.txt", ios::in | ios::out);
			AccountFile.seekg(ios::beg);
			AccountFile >> copy_account;
			while (!AccountFile.eof() && (strcmp(copy_account, game_account) != 0))
			{
				AccountFile >> copy_name
					>> copy_code
					>> copy_rank
					>> copy_experience
					>> copy_num;
				AccountFile >> copy_account;
			}
			ZeroMemory(sendbuf, BUF_SIZE);
			sendbuf[0] = 'Y';
			send(mysock, sendbuf, strlen(sendbuf), 0);

			ZeroMemory(recvebuf, BUF_SIZE);
			recv(mysock, recvebuf, BUF_SIZE, 0);
			memcpy(&que_or_passnum, recvebuf, 4);
			que_or_passnum--;
			ZeroMemory(sendbuf, BUF_SIZE);
			sendbuf[0] = 'Y';
			send(mysock, sendbuf, strlen(sendbuf), 0);

			int cur_experience;
			ZeroMemory(recvebuf, BUF_SIZE);
			recv(mysock, recvebuf, BUF_SIZE, 0);
			memcpy(&cur_experience, recvebuf, 4);
			cur_experience--;
			ZeroMemory(sendbuf, BUF_SIZE);
			sendbuf[0] = 'Y';
			send(mysock, sendbuf, strlen(sendbuf), 0);

			user_experience = user_experience + cur_experience;

			if (user_experience >= ((user_rank + 1)*INC_RANK_RATIO))
			{
				user_experience = user_experience - ((user_rank + 1)*INC_RANK_RATIO);
				user_rank++;
			}

			streampos position = AccountFile.tellg();
			AccountFile.seekp(position);
			AccountFile << " " << setw(PROPER_NUM) << setiosflags(ios::right) << setfill(' ') << user_name
				<< " " << setw(PROPER_NUM) << setiosflags(ios::right) << setfill(' ') << user_password
				<< " " << setw(PROPER_NUM) << setiosflags(ios::right) << setfill(' ') << user_rank
				<< " " << setw(PROPER_NUM) << setiosflags(ios::right) << setfill(' ') << user_experience
				<< " " << setw(PROPER_NUM) << setiosflags(ios::right) << setfill(' ') << que_or_passnum;
			AccountFile.close();
		}
	}
}

void listen_ans(LPVOID lpParameter)   //接收接收挑战方的回应
{
	char recvebuf[BUF_SIZE] = { '\0' };
	char sendbuf[BUF_SIZE] = { '\0' };

	int *port = (int *)lpParameter;
	if (listen_lab == TRUE);
	{
		ZeroMemory(recvebuf, BUF_SIZE);
		recv(*port, recvebuf, BUF_SIZE, 0);
		if (recvebuf[0] == 'Y')
		{
			all_sendbuf[0] = 'Y';
			return;
		}
		else
		{
			all_sendbuf[0] = 'N';
			return;
		}
	}
	while (listen_lab==TRUE)
	{		
	}
	return;
}