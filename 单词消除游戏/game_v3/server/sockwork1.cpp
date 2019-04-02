#include<iostream>
#include<fstream>
#include<string>
#include<iomanip>
#include<windows.h>
#include"mylib.h"
#include"sockwork.h"
using namespace std;

sockwork::sockwork()
	:user_experience(0), sort_standard(0), user_rank(0), que_or_passnum(0), mysock(-1), v_mysock1(-1), v_mysock2(-1)
{
	ZeroMemory(user_name, PROPER_NUM);
	ZeroMemory(game_account, PROPER_NUM);
	ZeroMemory(user_password, PROPER_NUM);
}

sockwork::sockwork(char *account, char *name, char *password,
	int experience, int standard, int rank, int num, int _role, int _sock, int _v_mysock1, int _v_mysock2)
	:user_experience(experience), sort_standard(standard),
	user_rank(rank), que_or_passnum(que_or_passnum), role(_role), 
	mysock(_sock), v_mysock1(_v_mysock1), v_mysock2(_v_mysock2)
{
	strcpy(game_account, account);
	strcpy(user_name, name);
	strcpy(user_password, password);
}

sockwork::sockwork(const sockwork& I)
	:user_experience(I.user_experience), sort_standard(I.sort_standard),
	user_rank(I.user_rank), que_or_passnum(I.que_or_passnum), role(I.role), 
	mysock(I.mysock), v_mysock1(I.v_mysock1), v_mysock2(I.v_mysock2)
{
	strcpy(game_account, I.game_account);
	strcpy(user_name, I.user_name);
	strcpy(user_password, I.user_password);
}

void sockwork::search_individual()   //按照属性查询玩家信息，传送给客户端
{
	int i = 0;
	int command = 0;
	char find_str[PROPER_NUM] = { '\0' };
	int find_int;
	string cur_inf1 = "player_information.txt";
	string cur_inf2 = "adm_information.txt";

	char recvebuf[BUF_SIZE], sendbuf[BUF_SIZE] = { "\0" };

	ZeroMemory(recvebuf, BUF_SIZE);
	recv(mysock, recvebuf, BUF_SIZE, 0);
	memcpy(&command, recvebuf, 4);        //接收内部的小命令
	ZeroMemory(sendbuf, BUF_SIZE);
	sendbuf[0] = 'Y';
	send(mysock, sendbuf, strlen(sendbuf), 0);
	if (command <= 2)
	{
		ZeroMemory(recvebuf, BUF_SIZE);
		recv(mysock, recvebuf, BUF_SIZE, 0);
		if (recvebuf[0] == '*')
			return;
		else
			strcpy(find_str, recvebuf);
	}
	else
	{
		ZeroMemory(recvebuf, BUF_SIZE);
		recv(mysock, recvebuf, BUF_SIZE, 0);
		memcpy(&find_int, recvebuf, 4);
		find_int--;
	}
	switch (command)
	{
	case 1:
		account_search(find_str, cur_inf1);
		ZeroMemory(recvebuf, BUF_SIZE);
		recv(mysock, recvebuf, BUF_SIZE, 0);
		account_search(find_str, cur_inf2);
		break;
	case 2:
		name_search(find_str, cur_inf1);
		ZeroMemory(recvebuf, BUF_SIZE);
		recv(mysock, recvebuf, BUF_SIZE, 0);
		name_search(find_str, cur_inf2);
		break;
	case 3:	
		rank_search(find_int, cur_inf1);
		ZeroMemory(recvebuf, BUF_SIZE);
		recv(mysock, recvebuf, BUF_SIZE, 0);
		rank_search(find_int, cur_inf2);
		break;
	case 4:
		exp_search(find_int, cur_inf1);
		ZeroMemory(recvebuf, BUF_SIZE);
		recv(mysock, recvebuf, BUF_SIZE, 0);
		exp_search(find_int, cur_inf2);
		break;
	case 5:
		num_search(find_int, cur_inf1);
		ZeroMemory(recvebuf, BUF_SIZE);
		recv(mysock, recvebuf, BUF_SIZE, 0);
		num_search(find_int, cur_inf2);
		break;
	default:break;
	}
}

void sockwork::account_search(char find_str[],string cur_inf)//按账户查询
{
	char recvebuf[BUF_SIZE], sendbuf[BUF_SIZE] = { "\0" };
	char copy_code[PROPER_NUM] = { "\0" };
	char copy_account[PROPER_NUM] = { "\0" };
	char copy_name[PROPER_NUM] = { "\0" };
	int copy_rank, rank, copy_experience, experience, copy_num, num;

	int i = 0;
	ifstream AccountFile1(cur_inf);
	while (!AccountFile1.eof())
	{
		AccountFile1 >> copy_account
			>> copy_name
			>> copy_code
			>> copy_rank
			>> copy_experience
			>> copy_num;
		if (strcmp(find_str, copy_account) == 0)
		{
			ZeroMemory(sendbuf, BUF_SIZE);
			strcpy(sendbuf, copy_account);
			send(mysock, sendbuf, strlen(sendbuf), 0);
			ZeroMemory(recvebuf, BUF_SIZE);
			recv(mysock, recvebuf, BUF_SIZE, 0);

			ZeroMemory(sendbuf, BUF_SIZE);
			strcpy(sendbuf, copy_name);
			send(mysock, sendbuf, strlen(sendbuf), 0);
			ZeroMemory(recvebuf, BUF_SIZE);
			recv(mysock, recvebuf, BUF_SIZE, 0);

			ZeroMemory(sendbuf, BUF_SIZE);
			copy_rank++;
			memcpy(sendbuf, &copy_rank, 4);
			send(mysock, sendbuf, strlen(sendbuf), 0);
			ZeroMemory(recvebuf, BUF_SIZE);
			recv(mysock, recvebuf, BUF_SIZE, 0);

			ZeroMemory(sendbuf, BUF_SIZE);
			copy_experience++;
			memcpy(sendbuf, &copy_experience, 4);
			send(mysock, sendbuf, strlen(sendbuf), 0);
			ZeroMemory(recvebuf, BUF_SIZE);
			recv(mysock, recvebuf, BUF_SIZE, 0);

			ZeroMemory(sendbuf, BUF_SIZE);
			copy_num++;
			memcpy(sendbuf, &copy_num, 4);
			send(mysock, sendbuf, strlen(sendbuf), 0);
			ZeroMemory(recvebuf, BUF_SIZE);
			recv(mysock, recvebuf, BUF_SIZE, 0);
		}
		
	}
	ZeroMemory(sendbuf, BUF_SIZE);
	sendbuf[0] = '-';
	sendbuf[1] = '>';
	send(mysock, sendbuf, strlen(sendbuf), 0);
}

void sockwork::name_search(char find_str[], string cur_inf)//按姓名查询
{
	char recvebuf[BUF_SIZE], sendbuf[BUF_SIZE] = { "\0" };
	char copy_code[PROPER_NUM] = { "\0" };
	char copy_account[PROPER_NUM] = { "\0" };
	char copy_name[PROPER_NUM] = { "\0" };
	int copy_rank, rank, copy_experience, experience, copy_num, num;
	int i = 0;
	ifstream AccountFile1(cur_inf);
	while (!AccountFile1.eof())
	{
		AccountFile1 >> copy_account
			>> copy_name
			>> copy_code
			>> copy_rank
			>> copy_experience
			>> copy_num;
		if (strcmp(find_str, copy_name) == 0)
		{
			ZeroMemory(sendbuf, BUF_SIZE);
			strcpy(sendbuf, copy_account);
			send(mysock, sendbuf, strlen(sendbuf), 0);
			ZeroMemory(recvebuf, BUF_SIZE);
			recv(mysock, recvebuf, BUF_SIZE, 0);

			ZeroMemory(sendbuf, BUF_SIZE);
			strcpy(sendbuf, copy_name);
			send(mysock, sendbuf, strlen(sendbuf), 0);
			ZeroMemory(recvebuf, BUF_SIZE);
			recv(mysock, recvebuf, BUF_SIZE, 0);

			ZeroMemory(sendbuf, BUF_SIZE);
			copy_rank++;
			memcpy(sendbuf, &copy_rank, 4);
			send(mysock, sendbuf, strlen(sendbuf), 0);
			ZeroMemory(recvebuf, BUF_SIZE);
			recv(mysock, recvebuf, BUF_SIZE, 0);

			ZeroMemory(sendbuf, BUF_SIZE);
			copy_experience++;
			memcpy(sendbuf, &copy_experience, 4);
			send(mysock, sendbuf, strlen(sendbuf), 0);
			ZeroMemory(recvebuf, BUF_SIZE);
			recv(mysock, recvebuf, BUF_SIZE, 0);

			ZeroMemory(sendbuf, BUF_SIZE);
			copy_num++;
			memcpy(sendbuf, &copy_num, 4);
			send(mysock, sendbuf, strlen(sendbuf), 0);
			ZeroMemory(recvebuf, BUF_SIZE);
			recv(mysock, recvebuf, BUF_SIZE, 0);
		}

	}
	ZeroMemory(sendbuf, BUF_SIZE);
	sendbuf[0] = '-';
	sendbuf[1] = '>';
	send(mysock, sendbuf, strlen(sendbuf), 0);
}

void sockwork::rank_search(int find_int, string cur_inf)//按等级查询
{
	char recvebuf[BUF_SIZE], sendbuf[BUF_SIZE] = { "\0" };
	char copy_code[PROPER_NUM] = { "\0" };
	char copy_account[PROPER_NUM] = { "\0" };
	char copy_name[PROPER_NUM] = { "\0" };
	int copy_rank, rank, copy_experience, experience, copy_num, num;
	int i = 0;
	ifstream AccountFile1(cur_inf);
	while (!AccountFile1.eof())
	{
		AccountFile1 >> copy_account
			>> copy_name
			>> copy_code
			>> copy_rank
			>> copy_experience
			>> copy_num;
		if (find_int==copy_rank)
		{
			ZeroMemory(sendbuf, BUF_SIZE);
			strcpy(sendbuf, copy_account);
			send(mysock, sendbuf, strlen(sendbuf), 0);
			ZeroMemory(recvebuf, BUF_SIZE);
			recv(mysock, recvebuf, BUF_SIZE, 0);

			ZeroMemory(sendbuf, BUF_SIZE);
			strcpy(sendbuf, copy_name);
			send(mysock, sendbuf, strlen(sendbuf), 0);
			ZeroMemory(recvebuf, BUF_SIZE);
			recv(mysock, recvebuf, BUF_SIZE, 0);

			ZeroMemory(sendbuf, BUF_SIZE);
			copy_rank++;
			memcpy(sendbuf, &copy_rank, 4);
			send(mysock, sendbuf, strlen(sendbuf), 0);
			ZeroMemory(recvebuf, BUF_SIZE);
			recv(mysock, recvebuf, BUF_SIZE, 0);

			ZeroMemory(sendbuf, BUF_SIZE);
			copy_experience++;
			memcpy(sendbuf, &copy_experience, 4);
			send(mysock, sendbuf, strlen(sendbuf), 0);
			ZeroMemory(recvebuf, BUF_SIZE);
			recv(mysock, recvebuf, BUF_SIZE, 0);

			ZeroMemory(sendbuf, BUF_SIZE);
			copy_num++;
			memcpy(sendbuf, &copy_num, 4);
			send(mysock, sendbuf, strlen(sendbuf), 0);
			ZeroMemory(recvebuf, BUF_SIZE);
			recv(mysock, recvebuf, BUF_SIZE, 0);
		}

	}
	ZeroMemory(sendbuf, BUF_SIZE);
	sendbuf[0] = '-';
	sendbuf[1] = '>';
	send(mysock, sendbuf, strlen(sendbuf), 0);
}

void sockwork::exp_search(int find_int, string cur_inf)//按经验查询
{
	char recvebuf[BUF_SIZE], sendbuf[BUF_SIZE] = { "\0" };
	char copy_code[PROPER_NUM] = { "\0" };
	char copy_account[PROPER_NUM] = { "\0" };
	char copy_name[PROPER_NUM] = { "\0" };
	int copy_rank, rank, copy_experience, experience, copy_num, num;
	int i = 0;
	ifstream AccountFile1(cur_inf);
	while (!AccountFile1.eof())
	{
		AccountFile1 >> copy_account
			>> copy_name
			>> copy_code
			>> copy_rank
			>> copy_experience
			>> copy_num;
		if (find_int==copy_experience)
		{
			ZeroMemory(sendbuf, BUF_SIZE);
			strcpy(sendbuf, copy_account);
			send(mysock, sendbuf, strlen(sendbuf), 0);
			ZeroMemory(recvebuf, BUF_SIZE);
			recv(mysock, recvebuf, BUF_SIZE, 0);

			ZeroMemory(sendbuf, BUF_SIZE);
			strcpy(sendbuf, copy_name);
			send(mysock, sendbuf, strlen(sendbuf), 0);
			ZeroMemory(recvebuf, BUF_SIZE);
			recv(mysock, recvebuf, BUF_SIZE, 0);

			ZeroMemory(sendbuf, BUF_SIZE);
			copy_rank++;
			memcpy(sendbuf, &copy_rank, 4);
			send(mysock, sendbuf, strlen(sendbuf), 0);
			ZeroMemory(recvebuf, BUF_SIZE);
			recv(mysock, recvebuf, BUF_SIZE, 0);

			ZeroMemory(sendbuf, BUF_SIZE);
			copy_experience++;
			memcpy(sendbuf, &copy_experience, 4);
			send(mysock, sendbuf, strlen(sendbuf), 0);
			ZeroMemory(recvebuf, BUF_SIZE);
			recv(mysock, recvebuf, BUF_SIZE, 0);

			ZeroMemory(sendbuf, BUF_SIZE);
			copy_num++;
			memcpy(sendbuf, &copy_num, 4);
			send(mysock, sendbuf, strlen(sendbuf), 0);
			ZeroMemory(recvebuf, BUF_SIZE);
			recv(mysock, recvebuf, BUF_SIZE, 0);
		}

	}
	ZeroMemory(sendbuf, BUF_SIZE);
	sendbuf[0] = '-';
	sendbuf[1] = '>';
	send(mysock, sendbuf, strlen(sendbuf), 0);
}

void sockwork::num_search(int find_int, string cur_inf)//按出题数或者闯关数查询
{
	char recvebuf[BUF_SIZE], sendbuf[BUF_SIZE] = { "\0" };
	char copy_code[PROPER_NUM] = { "\0" };
	char copy_account[PROPER_NUM] = { "\0" };
	char copy_name[PROPER_NUM] = { "\0" };
	int copy_rank, rank, copy_experience, experience, copy_num, num;
	int i = 0;
	ifstream AccountFile1(cur_inf);
	while (!AccountFile1.eof())
	{
		AccountFile1 >> copy_account
			>> copy_name
			>> copy_code
			>> copy_rank
			>> copy_experience
			>> copy_num;
		if (find_int==copy_num)
		{
			ZeroMemory(sendbuf, BUF_SIZE);
			strcpy(sendbuf, copy_account);
			send(mysock, sendbuf, strlen(sendbuf), 0);
			ZeroMemory(recvebuf, BUF_SIZE);
			recv(mysock, recvebuf, BUF_SIZE, 0);

			ZeroMemory(sendbuf, BUF_SIZE);
			strcpy(sendbuf, copy_name);
			send(mysock, sendbuf, strlen(sendbuf), 0);
			ZeroMemory(recvebuf, BUF_SIZE);
			recv(mysock, recvebuf, BUF_SIZE, 0);

			ZeroMemory(sendbuf, BUF_SIZE);
			copy_rank++;
			memcpy(sendbuf, &copy_rank, 4);
			send(mysock, sendbuf, strlen(sendbuf), 0);
			ZeroMemory(recvebuf, BUF_SIZE);
			recv(mysock, recvebuf, BUF_SIZE, 0);

			ZeroMemory(sendbuf, BUF_SIZE);
			copy_experience++;
			memcpy(sendbuf, &copy_experience, 4);
			send(mysock, sendbuf, strlen(sendbuf), 0);
			ZeroMemory(recvebuf, BUF_SIZE);
			recv(mysock, recvebuf, BUF_SIZE, 0);

			ZeroMemory(sendbuf, BUF_SIZE);
			copy_num++;
			memcpy(sendbuf, &copy_num, 4);
			send(mysock, sendbuf, strlen(sendbuf), 0);
			ZeroMemory(recvebuf, BUF_SIZE);
			recv(mysock, recvebuf, BUF_SIZE, 0);
		}

	}
	ZeroMemory(sendbuf, BUF_SIZE);
	sendbuf[0] = '-';
	sendbuf[1] = '>';
	send(mysock, sendbuf, strlen(sendbuf), 0);
}

void sockwork::work()         //该函数接收客户端的各个请求，然后调用不同的模块函数，对请求进行处理
{

	char recvebuf[BUF_SIZE], sendbuf[BUF_SIZE] = { "\0" };

	  int command;
	  while (true)
	  {
		  //接收客户端数据
		  ZeroMemory(recvebuf, BUF_SIZE);
		  int lab=recv(mysock, recvebuf, BUF_SIZE, 0);
		  if (SOCKET_ERROR == lab)
		  {
			  cout << "一个客户端已经断开连接"<<endl;
			  back();
			  mysock = -1;
			  v_mysock1 = -1;
			  v_mysock2 = -1;
			  closesocket(mysock);	//关闭套接字		
			  return;
		  }
		  memcpy(&command, recvebuf, 4);
		  switch (command)
		  {
		  case CHANGE_NAME:

			  ZeroMemory(sendbuf, BUF_SIZE);
			  sendbuf[0] = 'Y';
			  send(mysock, sendbuf, strlen(sendbuf), 0);
			  change_username();

			  break;
		  case CHANGE_PASSWORD:
			  ZeroMemory(sendbuf, BUF_SIZE);
			  sendbuf[0] = 'Y';
			  send(mysock, sendbuf, strlen(sendbuf), 0);
			  change_password();
			  break;
		  case REGISTER:
			  ZeroMemory(sendbuf, BUF_SIZE);
			  sendbuf[0] = 'Y';
			  send(mysock, sendbuf, strlen(sendbuf), 0);
			  user_register();
			  break;
		  case LOGIN:
			  ZeroMemory(sendbuf, BUF_SIZE);
			  sendbuf[0] = 'Y';
			  send(mysock, sendbuf, strlen(sendbuf), 0);
			  user_login();
			  break;
		  case SEARCH_ALL:
			  ZeroMemory(sendbuf, BUF_SIZE);
			  sendbuf[0] = 'Y';
			  send(mysock, sendbuf, strlen(sendbuf), 0);
			  search_All_individual();
			  break;
		  case SEARCH_ONES:
			  ZeroMemory(sendbuf, BUF_SIZE);
			  sendbuf[0] = 'Y';
			  send(mysock, sendbuf, strlen(sendbuf), 0);
			  search_individual();
			  break;
		  case CHANGE:
			  ZeroMemory(sendbuf, BUF_SIZE);
			  sendbuf[0] = 'Y';
			  send(mysock, sendbuf, strlen(sendbuf), 0);
			  change();
			  break;
		  case SORT:
			  ZeroMemory(sendbuf, BUF_SIZE);
			  sendbuf[0] = 'Y';
			  send(mysock, sendbuf, strlen(sendbuf), 0);
			  sort();
			  break;
		  case SEARCH_LOG:
			  ZeroMemory(sendbuf, BUF_SIZE);
			  sendbuf[0] = 'Y';
			  send(mysock, sendbuf, strlen(sendbuf), 0);
			  search_log();
			  break;
		  case DO_CHALLANGE:
			  ZeroMemory(sendbuf, BUF_SIZE);
			  sendbuf[0] = 'Y';
			  send(mysock, sendbuf, strlen(sendbuf), 0);
			  challange();
			  break;
		  case BACK:
			  back();
			  ZeroMemory(sendbuf, BUF_SIZE);
			  sendbuf[0] = 'Y';
			  send(mysock, sendbuf, strlen(sendbuf), 0);
			  break;
		  case END_BACK:
			  cout << "一个客户端断开连接"<<endl;
			  mysock = -1;
			  v_mysock1 = -1;
			  v_mysock2 = -1;
			  closesocket(mysock);	//关闭套接字
			  return;
			  break;
		  }
	  }
}

void sockwork::back()    //对账号退出事件进行处理
{
	char copy_account[PROPER_NUM] = { "\0" },
		copy_name[PROPER_NUM] = { "\0" };

	int copy_login_suc, copy_role,copy_port1,copy_port2,copy_port3;
	fstream AccountFile("login_score.txt", ios::in | ios::out);
	AccountFile.seekg(ios::beg);

	AccountFile >> copy_account
		>> copy_name
		>> copy_role;

	while (!AccountFile.eof() && ((strcmp(copy_account, game_account) != 0) || (role != copy_role)))
	{
		AccountFile>>copy_port1
			>> copy_port2
			>>copy_port3
			>> copy_login_suc;
		AccountFile >> copy_account
			>> copy_name
			>> copy_role;
	}
	if ((strcmp(copy_account, game_account) == 0) && (role == copy_role))
	{
		streampos position = AccountFile.tellg();
		AccountFile.seekp(position);
		AccountFile << " " << setw(PROPER_NUM) << setiosflags(ios::right) << setfill(' ') << copy_port1
			<< " " << setw(PROPER_NUM) << setiosflags(ios::right) << setfill(' ') << copy_port2
			<< " " << setw(PROPER_NUM) << setiosflags(ios::right) << setfill(' ') << copy_port3
			<< " " << setw(PROPER_NUM) << setiosflags(ios::right) << setfill(' ') << FALSE;
	}
	AccountFile.close();
	if (role == PLAYER)
	{
		cout << "闯关者账号" << game_account << "退出" << endl;
	}
	else if (role==SET_QUE_MAN)
	{
		cout << "出题者账号" << game_account << "退出" << endl;
	}
}

void run_client(LPVOID lpParameter)
{
	sockwork *client = (sockwork *)lpParameter;
	client->work();
		return;
}