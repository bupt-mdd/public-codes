#include<iostream>
#include<fstream>
#include<string>
#include<iomanip>
#include<windows.h>
#include"mylib.h"
#include"sockwork.h"
using namespace std;

void sockwork::change_username()      //玩家姓名修改
{

	char recvebuf[BUF_SIZE], sendbuf[BUF_SIZE] = { "\0" };
	string cur_inf;
	if (role == SET_QUE_MAN)
		cur_inf = "adm_information.txt";
	else
		cur_inf = "player_information.txt";
	ZeroMemory(recvebuf, BUF_SIZE);
	recv(mysock ,recvebuf, BUF_SIZE, 0);
	if (recvebuf[0] != '*')
	{
		char copy_account[PROPER_NUM] = {"\0"}, 
			 copy_name[PROPER_NUM] = { "\0" },
			 copy_code[PROPER_NUM] = { "\0" };

		int copy_rank, copy_experience, copy_num;
		fstream AccountFile(cur_inf, ios::in | ios::out);
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
		streampos position = AccountFile.tellg();
		ZeroMemory(user_name, PROPER_NUM);
		strcpy(user_name, recvebuf);
		AccountFile.seekp(position);
		AccountFile << " " << setw(PROPER_NUM) << setiosflags(ios::right) << setfill(' ') << user_name;
		AccountFile.close();

		int copy_login_suc, copy_role, copy_port1, copy_port2, copy_port3;
		fstream AccountFile1("login_score.txt", ios::in | ios::out);
		AccountFile1.seekg(ios::beg);

		AccountFile1 >> copy_account;
		position = AccountFile1.tellg();
		AccountFile1 >> copy_name
			>> copy_role
			>> copy_port1
			>> copy_port2
			>> copy_port3
			>> copy_login_suc;

		while (!AccountFile1.eof() && ((strcmp(copy_account, game_account) != 0)||(copy_role!=role)))
		{
			AccountFile1 >> copy_account;
			position = AccountFile1.tellg();
			AccountFile1 >> copy_name
				>> copy_role
				>> copy_port1
				>> copy_port2
				>> copy_port3
				>> copy_login_suc;
		}
		if ((strcmp(copy_account, game_account) == 0) && (copy_role == role))
		{
			AccountFile1.seekp(position);
			AccountFile1 << " " << setw(PROPER_NUM) << setiosflags(ios::right) << setfill(' ') << user_name;
			AccountFile1.close();
		}

		ZeroMemory(sendbuf, BUF_SIZE);
		sendbuf[0] = 'Y';
		send(mysock, sendbuf, strlen(sendbuf), 0);
	}

}

void sockwork::change_password()       //玩家密码修改
{
	char recvebuf[BUF_SIZE], sendbuf[BUF_SIZE] = { "\0" };
	string cur_inf;
	if (role == SET_QUE_MAN)
		cur_inf = "adm_information.txt";
	else
		cur_inf = "player_information.txt";

	ZeroMemory(recvebuf, BUF_SIZE);
	recv(mysock, recvebuf, BUF_SIZE, 0);
	if (recvebuf[0] != '*')
	{
		string copy_account, copy_name, copy_code;
		int copy_rank, copy_experience, copy_num;
		fstream AccountFile(cur_inf, ios::in | ios::out);
		AccountFile.seekg(ios::beg);

		AccountFile >> copy_account;
		while (!AccountFile.eof() && (copy_account != game_account))
		{
			AccountFile >> copy_name
				>> copy_code
				>> copy_rank
				>> copy_experience
				>> copy_num;
			AccountFile >> copy_account;
		}
		streampos position = AccountFile.tellg();
		ZeroMemory(user_password, PROPER_NUM);
		strcpy(user_password , recvebuf);
		AccountFile.seekp(position);
		AccountFile << " " << setw(PROPER_NUM) << setiosflags(ios::right) << setfill(' ') << user_name
			        << " " << setw(PROPER_NUM) << setiosflags(ios::right) << setfill(' ') << user_password;
		AccountFile.close();
		ZeroMemory(sendbuf, BUF_SIZE);
		sendbuf[0] = 'Y';
		send(mysock, sendbuf, strlen(sendbuf), 0);
	}

}  

void sockwork::user_register()      //玩家注册
{
	char recvebuf[BUF_SIZE], sendbuf[BUF_SIZE] = { "\0" };
	ZeroMemory(recvebuf, BUF_SIZE);
	recv(mysock, recvebuf, BUF_SIZE, 0);
	if (recvebuf[0]!='*')
	{
		memcpy(&role, recvebuf, 4);
		string cur_inf;
		if (role == SET_QUE_MAN)
			cur_inf = "adm_information.txt";
		else
			cur_inf = "player_information.txt";

		ZeroMemory(sendbuf, BUF_SIZE);
		sendbuf[0] = 'Y';
		send(mysock, sendbuf, strlen(sendbuf), 0);

		ZeroMemory(recvebuf, BUF_SIZE);
		recv(mysock, recvebuf, BUF_SIZE, 0);

		string account, old_account = { "\0" };
		account = recvebuf;
		ifstream AccountFile1(cur_inf, ios::in);
		char other_inf[MAXNUM_STR];
		while (!AccountFile1.eof() && (old_account != account))
		{
			AccountFile1 >> old_account;
			AccountFile1.getline(other_inf, MAXNUM_STR);
		}
		AccountFile1.close();
		if (old_account != account)
		{
			ZeroMemory(game_account, PROPER_NUM);
			strcpy(game_account, recvebuf);
			 
			ZeroMemory(sendbuf, BUF_SIZE);
			sendbuf[0] = 'Y';
			send(mysock, sendbuf, strlen(sendbuf), 0);
			ZeroMemory(recvebuf, BUF_SIZE);
			recv(mysock, recvebuf, BUF_SIZE, 0);
			ZeroMemory(user_name, PROPER_NUM);
			strcpy(user_name, recvebuf);

			send(mysock, sendbuf, strlen(sendbuf), 0);
			ZeroMemory(recvebuf, BUF_SIZE);
			recv(mysock, recvebuf, BUF_SIZE, 0);
			ZeroMemory(user_password, PROPER_NUM);
			strcpy(user_password, recvebuf);

			ofstream AccountFile2(cur_inf, ios::app | ios::out);
			AccountFile2
				<< endl << setw(PROPER_NUM) << setiosflags(ios::right) << game_account
				<< " " << setw(PROPER_NUM) << setiosflags(ios::right) << user_name
				<< " " << setw(PROPER_NUM) << setiosflags(ios::right) << user_password
				<< " " << setw(PROPER_NUM) << setiosflags(ios::right) << user_rank
				<< " " << setw(PROPER_NUM) << setiosflags(ios::right) << user_experience
				<< " " << setw(PROPER_NUM) << setiosflags(ios::right) << que_or_passnum;
			AccountFile2.close();
			ZeroMemory(sendbuf, BUF_SIZE);
			sendbuf[0] = 'Y';
			send(mysock, sendbuf, strlen(sendbuf), 0);
		}
		else
		{
			ZeroMemory(sendbuf, BUF_SIZE);
			sendbuf[0] = 'N';
			send(mysock, sendbuf, strlen(sendbuf), 0);
		}
	}
}    

void sockwork::user_login()          //实现玩家登陆
{
	char recvebuf[BUF_SIZE], sendbuf[BUF_SIZE] = { "\0" };
	ZeroMemory(recvebuf, BUF_SIZE);
	recv(mysock, recvebuf, BUF_SIZE, 0);

	if (recvebuf[0] != '*')
	{
		memcpy(&role, recvebuf, 4);
		string cur_inf;
		if (role == SET_QUE_MAN)
			cur_inf = "adm_information.txt";
		else
			cur_inf = "player_information.txt";

		char account[PROPER_NUM] = { "\0" };
		int copy_rank, copy_experience, copy_num;
		ZeroMemory(sendbuf, BUF_SIZE);
		sendbuf[0] = 'Y';
		send(mysock, sendbuf, strlen(sendbuf), 0);
		ZeroMemory(recvebuf, BUF_SIZE);
		recv(mysock, recvebuf, BUF_SIZE, 0);
		ZeroMemory(account, PROPER_NUM);
		strcpy(account , recvebuf);

		ifstream AccountFile1(cur_inf);
		char copy_account[PROPER_NUM] = {"\0"},
			   copy_name[PROPER_NUM] = {"\0"},
			   copy_code[PROPER_NUM] = {"\0"};

		AccountFile1 >> copy_account
			>> copy_name
			>> copy_code
			>> copy_rank
			>> copy_experience
			>> copy_num;
		while (!AccountFile1.eof() && (strcmp(copy_account , account)!=0))
		{
			AccountFile1 >> copy_account
				>> copy_name
				>> copy_code
				>> copy_rank
				>> copy_experience
				>> copy_num;
		}
		AccountFile1.close();
		if (strcmp(copy_account, account) == 0)
		{
			ZeroMemory(sendbuf, BUF_SIZE);
			sendbuf[0] = 'Y';
			send(mysock, sendbuf, strlen(sendbuf), 0);
			ZeroMemory(recvebuf, BUF_SIZE);
			recv(mysock, recvebuf, BUF_SIZE, 0);
			char code[PROPER_NUM] = {"\0"}; 
			strcpy(code, recvebuf);
			if (strcmp(copy_code , code)==0)
			{
				ZeroMemory(sendbuf, BUF_SIZE);
				sendbuf[0] = 'Y';
				send(mysock, sendbuf, strlen(sendbuf), 0);

				ZeroMemory(game_account, PROPER_NUM);
				strcpy(game_account, copy_account);
				ZeroMemory(user_password, PROPER_NUM);
				strcpy(user_password, copy_code);

				ZeroMemory(user_name, PROPER_NUM);
				strcpy(user_name, copy_name);

				recv(mysock, recvebuf, BUF_SIZE, 0);
				ZeroMemory(sendbuf, BUF_SIZE);
				strcpy(sendbuf,copy_name);
				send(mysock, sendbuf, strlen(sendbuf), 0);

				user_rank = copy_rank;
				copy_rank++;
				recv(mysock, recvebuf, BUF_SIZE, 0);
				ZeroMemory(sendbuf, BUF_SIZE);
				memcpy(sendbuf, &copy_rank, 4);
				send(mysock, sendbuf, strlen(sendbuf), 0);

				user_experience = copy_experience;
				copy_experience++;
				recv(mysock, recvebuf, BUF_SIZE, 0);
				ZeroMemory(sendbuf, BUF_SIZE);
				memcpy(sendbuf, &copy_experience, 4);
				send(mysock, sendbuf, strlen(sendbuf), 0);

				que_or_passnum = copy_num;
				copy_num++;
				recv(mysock, recvebuf, BUF_SIZE, 0);
				ZeroMemory(sendbuf, BUF_SIZE);
				memcpy(sendbuf, &copy_num, 4);
				send(mysock, sendbuf, strlen(sendbuf), 0);

				char copy_account[PROPER_NUM] = { "\0" },
					copy_name[PROPER_NUM] = { "\0" };

				int copy_login_suc, copy_role,copy_port1,copy_port2,copy_port3;
				fstream AccountFile("login_score.txt", ios::in | ios::out);
				streampos position;
				AccountFile.seekg(ios::beg);

				AccountFile >> copy_account
					>> copy_name
					>> copy_role;
				position = AccountFile.tellg();
				AccountFile >> copy_port1
					        >>copy_port2
							>>copy_port3
					        >> copy_login_suc;

				while (!AccountFile.eof() && ((strcmp(copy_account, game_account) != 0) || (role != copy_role)))
				{
					AccountFile >> copy_account
						>> copy_name
						>> copy_role;
					position = AccountFile.tellg();
					AccountFile >> copy_port1
						        >>copy_port2
								>>copy_port3
						        >> copy_login_suc;
				}
				if ((strcmp(copy_account, game_account) == 0) && (role == copy_role))
				{
					if (copy_login_suc == FALSE)
					{
						int login_suc = TRUE;
						AccountFile.seekp(position);
						AccountFile << " " << setw(PROPER_NUM) << setiosflags(ios::right) << mysock
							        << " " << setw(PROPER_NUM) << setiosflags(ios::right) << v_mysock1
									<< " " << setw(PROPER_NUM) << setiosflags(ios::right) << v_mysock2
							        << " " << setw(PROPER_NUM) << setiosflags(ios::right) << login_suc;
						AccountFile.close();

						recv(mysock, recvebuf, BUF_SIZE, 0);
						ZeroMemory(sendbuf, BUF_SIZE);
						sendbuf[0] = 'Y';
						send(mysock, sendbuf, strlen(sendbuf), 0);

						if (role == PLAYER)
						{
							cout << "闯关者账号" << game_account << "登陆成功" << endl;
						}
						else
							cout << "出题者账号" << game_account << "登陆成功" << endl;
					}
					else
					{
						recv(mysock, recvebuf, BUF_SIZE, 0);
						ZeroMemory(sendbuf, BUF_SIZE);
						sendbuf[0] = 'N';
						send(mysock, sendbuf, strlen(sendbuf), 0);
					}
				}
				else
				{
					AccountFile.close();
					int login_suc = TRUE;
					ofstream AccountFile2("login_score.txt",ios::app|ios::out);
					AccountFile2<< setw(PROPER_NUM) << setiosflags(ios::right) << game_account
						<< " " << setw(PROPER_NUM) << setiosflags(ios::right) << user_name
						<< " " << setw(PROPER_NUM) << setiosflags(ios::right) << role
						<< " " << setw(PROPER_NUM) << setiosflags(ios::right) << mysock
						<< " " << setw(PROPER_NUM) << setiosflags(ios::right) << v_mysock1
						<< " " << setw(PROPER_NUM) << setiosflags(ios::right) << v_mysock2
						<< " " << setw(PROPER_NUM) << setiosflags(ios::right) << login_suc<<endl;
					AccountFile2.close();

					recv(mysock, recvebuf, BUF_SIZE, 0);
					ZeroMemory(sendbuf, BUF_SIZE);
					sendbuf[0] = 'Y';
					send(mysock, sendbuf, strlen(sendbuf), 0);

					if (role == PLAYER)
					{
						cout << "闯关者账号" << game_account << "登陆成功" << endl;
					}
					else
						cout << "出题者账号" << game_account << "登陆成功" << endl;
				}
			}
			else
			{
				ZeroMemory(sendbuf, BUF_SIZE);
				sendbuf[0] = 'N';
				send(mysock, sendbuf, strlen(sendbuf), 0);
			}
		}
		else
		{
			ZeroMemory(sendbuf, BUF_SIZE);
			sendbuf[0] = 'N';
			send(mysock, sendbuf, strlen(sendbuf), 0);
		}
	}
}


