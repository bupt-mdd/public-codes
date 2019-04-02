#include<iostream>
#include<fstream>
#include<string>
#include<iomanip>
#include<windows.h>
#include<time.h>
#include"mylib.h"
#include"individual.h"
#include"wordpool.h"
#include"gamer.h"
using namespace std;

void gamer::listen()
{
	char recvebuf[BUF_SIZE], sendbuf[BUF_SIZE] = { "\0" };
	char copy_account[MAX_ARRAY_NUM] = { '\0' };
	char account[MAX_ARRAY_NUM] = { '\0' };
	char copy_name[MAX_ARRAY_NUM] = { '\0' };
	char name[MAX_ARRAY_NUM] = { '\0' };

	while (true)
	{
		Sleep(1);
		while (listen_lab == SET_QUE_MAN)
			Sleep(1000);
		ZeroMemory(recvebuf, BUF_SIZE);
		recv(v_client1, recvebuf, BUF_SIZE, 0);
		int command;
		memcpy(&command, recvebuf, 4);
		if(command==REC_CHALLANGE)
		{
			if (challange_lab==FALSE)
			{
				if (whether != FALSE)
				{
					ZeroMemory(sendbuf, BUF_SIZE);
					sendbuf[0] = 'N';
					send(v_client1, sendbuf, strlen(sendbuf), 0);//发送确认
				}
				else
				{
					ZeroMemory(sendbuf, BUF_SIZE);
					sendbuf[0] = 'Y';
					send(v_client1, sendbuf, strlen(sendbuf), 0);//发送确认
					ZeroMemory(recvebuf, BUF_SIZE);
					recv(v_client1, recvebuf, BUF_SIZE, 0);//接收挑战者的账号名
					strcpy(challange_account, recvebuf);

					ZeroMemory(sendbuf, BUF_SIZE);
					sendbuf[0] = 'Y';
					send(v_client1, sendbuf, strlen(sendbuf), 0);//发送确认
					ZeroMemory(recvebuf, BUF_SIZE);
					recv(v_client1, recvebuf, BUF_SIZE, 0);//接收挑战者的姓名
					strcpy(challange_name, recvebuf);

					whether = TRUE;
					cout << endl << "消息类提示" << challange_account << "向你发起了挑战" << endl;
				}
			}
			else
			{
				ZeroMemory(sendbuf, BUF_SIZE);
				sendbuf[0] = 'N';
				sendbuf[1] = 'N';
				send(v_client1, sendbuf, strlen(sendbuf), 0);//发送确认
			}
		} 
		else
		{
			if (close != FALSE)
				return;             //通过return结束该线程
			whether = FALSE;
			cout << endl << "消息类提示：" << challange_account << "取消了对你的挑战" << endl;
		}
	}
}

void gamer::rec_challange()
{
	system("cls");
	clock_t starttimer, stoptimer;
	
	char in_word[MAX_WORD_NUM + 1];
	char word[MAX_WORD_NUM + 1];
	char recvebuf[BUF_SIZE];
    char sendbuf[BUF_SIZE] = { "\0" };
	
	char cmd_str[BUF_SIZE];
	char cmd;
	if (whether == FALSE)
	{
		cout << "此时没有挑战者向你发出挑战" << endl;
	}
	else
	{
		cout << "以下是向你发起挑战的挑战者信息" << endl;
		cout << "账号为：" << challange_account << " ";
		cout << "姓名为：" << challange_name << endl;
		cout << "是否继续（继续--------Y      退出--------任意键）" << endl;
		cin >> cmd_str;

		if ((cmd_str[0] != 'Y' )&&( cmd_str[0] != 'y'))
		{
			cout << "成功退出接收挑战者界面" << endl;
		}
		else
		{
			int command;
			cout << "********************************************************" << endl;
			cout << "*                    请选择操作                        *" << endl;
			cout << "*    1接收挑战        2拒绝挑战          3退出         *" << endl;
			cout << "********************************************************" << endl;
			cin >> cmd_str;
			cmd = cmd_str[0];
			command = transfer_cmd(cmd);
			cout << "等待系统确认中..........." << endl;
			while (command != 3)
			{
				if (command == 1)
				{
					whether = 0;
					ZeroMemory(sendbuf, BUF_SIZE);
					sendbuf[0] = 'Y';
					send(v_client2, sendbuf, strlen(sendbuf), 0);

					ZeroMemory(recvebuf, BUF_SIZE);
					recv(client, recvebuf, BUF_SIZE, 0);//接收单词
					strcpy(word, recvebuf);
					system("cls");
					cout << "挑战开始" << endl;
					cout << "请先用心记忆下面这个单词" << endl << word;

					ZeroMemory(sendbuf, BUF_SIZE);
					sendbuf[0] = 'Y';
					send(v_client2, sendbuf, strlen(sendbuf), 0);//接收到单词后作出回应

					ZeroMemory(recvebuf, BUF_SIZE);
					recv(v_client2, recvebuf, BUF_SIZE, 0);//接收命令后进行清屏。

					system("cls");
					cout << "请输入刚才所显示单词" << endl;
					starttimer = clock();
					char ch;
					cin.get(ch);
					cin.get(ch);
					int LetterNum;
					for (LetterNum = 0; (ch != '\n') && (LetterNum < MAX_WORD_NUM); LetterNum++)
					{
						in_word[LetterNum] = ch;
						cin.get(ch);
					}
					in_word[LetterNum] = '\0';
					if (strcomp(in_word, word) == TRUE)
					{
						stoptimer = clock();
						float time = ((double)(stoptimer - starttimer)) / CLK_TCK;
						time = time + 1;

						cout << "等待系统判别中..........." << endl;
						ZeroMemory(sendbuf, BUF_SIZE);
						memcpy(sendbuf, &time, 4);
						send(v_client2, sendbuf, strlen(sendbuf), 0);//把所用时间发过去
						ZeroMemory(recvebuf, BUF_SIZE);
						recv(v_client2, recvebuf, BUF_SIZE, 0);//接收失败或者成功的确认

						if (recvebuf[0] == 'N')                //对方挑战失败
						{
							int cur_experience = (int)(get_num()*(INC_PLAYER_EXPER_RATIO / (time - 1))) * 2;//经验增长是平时的两倍
							change(PLAYER, get_num(), cur_experience);
						}
						else                                    //对方挑战成功。
						{
							int cur_experience = (int)(get_num()*(INC_PLAYER_EXPER_RATIO / (time - 1))) * (-2);
							change(PLAYER, get_num(), cur_experience);//失败后，会扣除原来的两倍经验
						}

						system("cls");
						if (recvebuf[0] == 'Y')
							cout << "对方挑战成功" << endl;
						else
							cout << "对方挑战失败" << endl;
					}
					else
					{
						stoptimer = clock();
						float time = ((double)(stoptimer - starttimer)) / CLK_TCK;
						time = time + 1;

						cout << "输入错误" << endl;
						ZeroMemory(sendbuf, BUF_SIZE);//把输入错误的N标志发过去。
						sendbuf[0] = 'N';
						send(v_client2, sendbuf, strlen(sendbuf), 0);
						ZeroMemory(recvebuf, BUF_SIZE);
						recv(v_client2, recvebuf, BUF_SIZE, 0);//接收对方挑战是否成功的确认

						if (recvebuf[0] == 'N')//对方挑战失败
						{
							int cur_experience = (int)(get_num()*(INC_PLAYER_EXPER_RATIO / (time - 1))) * 2;//经验增长是平时的两倍
							change(PLAYER, get_num(), cur_experience);
						}
						else                    //对方挑战成功。
						{
							int cur_experience = (int)(get_num()*(INC_PLAYER_EXPER_RATIO / (time - 1))) * (-2);
							change(PLAYER, get_num(), cur_experience);//失败后，会扣除原来的两倍经验
						}
					}

					break;
				}
				else if (command == 2)
				{
					whether = 0;
					ZeroMemory(sendbuf, BUF_SIZE);
					sendbuf[0] = 'N';
					send(v_client2, sendbuf, strlen(sendbuf), 0);
					break;
				}
				system("cls");
				cout << "********************************************************" << endl;
				cout << "*                    请选择操作                        *" << endl;
				cout << "*    1接收挑战        2拒绝挑战          3退出         *" << endl;
				cout << "********************************************************" << endl;
				cin >> cmd_str;
				cmd = cmd_str[0];
				command = transfer_cmd(cmd);
				cout << "等待系统确认中..........." << endl;
			}
		}
	}
}

void gamer::do_challange(word_pool e_pool, word_pool m_pool, word_pool d_pool)
{
	challange_lab = TRUE;
	int command;
	char cmd;
	char cmd_str[MAX_ARRAY_NUM] = { '\0' };
	char copy_account[MAX_ARRAY_NUM] = { '\0' };
	char recvebuf[BUF_SIZE], sendbuf[BUF_SIZE] = { "\0" };
	clock_t starttimer, stoptimer;
	command = 1;

		insearch_logon(PLAYER);
		int in_command = DO_CHALLANGE;
		ZeroMemory(sendbuf, BUF_SIZE);
		memcpy(sendbuf,&in_command ,4);
		send(client, sendbuf, strlen(sendbuf), 0);
		ZeroMemory(recvebuf, BUF_SIZE);
		recv(client, recvebuf, BUF_SIZE, 0);

		cout << "请选择并输入挑战者序号，输入英文“->”号退" << endl;
		cin >> copy_account;
		char *account = get_account();
		while (strcmp(copy_account, account) == 0)
		{
			cout << "不能对自己进行挑战" << endl;
			cout << "重新输入,输入英文“->”号退出" << endl;
			cin >> copy_account;
		}

		ZeroMemory(sendbuf, BUF_SIZE);
		strcpy(sendbuf,copy_account);
		send(client, sendbuf, strlen(sendbuf), 0);
		while (1)
		{ 
			ZeroMemory(recvebuf, BUF_SIZE);
			recv(client, recvebuf, BUF_SIZE, 0);
			if (recvebuf[0] == 'n')
			{
				int in_cmd;
				cout << "********************************************************" << endl;
				cout << "*                    请选择操作                        *" << endl;
				cout << "*      1等待对方应答             2退出并取消挑战       *" << endl;
				cout << "********************************************************" << endl;
				cin >> cmd_str;
				cmd = cmd_str[0];
				in_cmd = transfer_cmd(cmd);
				cout << "等待对方应答中..........." << endl;
				if (in_cmd == 2)
				{
					ZeroMemory(sendbuf, BUF_SIZE);
					sendbuf[0] = 'N';
					send(client, sendbuf, strlen(sendbuf), 0);
					challange_lab = FALSE;
					system("cls");
					break;
				}
				else
				{
					ZeroMemory(sendbuf, BUF_SIZE);
					sendbuf[0] = 'Y';
					send(client, sendbuf, strlen(sendbuf), 0);
				}
			}
			else if (recvebuf[0] == 'N')
			{
				if ((copy_account[0] == '-') && (copy_account[1] == '>'))
				{
				}
				else if ((recvebuf[0] == 'N') && (recvebuf[1] == 'N') && (recvebuf[2] == 'N') && (recvebuf[3] == 'N'))
					cout << "该闯关者并不在线" << endl;
				else if ((recvebuf[0] == 'N') && (recvebuf[1] == 'N') && (recvebuf[2] == 'N'))
					cout << "该玩家正在挑战别的玩家" << endl;
				else if ((recvebuf[0] == 'N') && (recvebuf[1] == 'N'))
					cout << "有别的玩家正在挑战该玩家" << endl;
				else
					cout << "对方拒绝接收挑战," << endl;
				
				challange_lab = FALSE;
				break;
			}
			else
			{

				char **word = NULL;
				word = new char*[WORD_NUM];
				for (int i = 0; i < WORD_NUM; i++)
				{
					word[i] = new char[MAX_WORD_NUM + 1];
				}
				e_pool.rand_word(word, 0, 0);//从单词池里边接收出一个单词出来。

				ZeroMemory(sendbuf, BUF_SIZE);
				strcpy(sendbuf, word[0]);
				send(client, sendbuf, strlen(sendbuf), 0);//把该单词发送给服务器
				system("cls");
				cout << "挑战开始" << endl;
				cout << "请用心记忆下边这个单词" << endl;
				cout << word[0];
				ZeroMemory(recvebuf, BUF_SIZE);
				recv(client, recvebuf, BUF_SIZE, 0);//等地服务器的清屏命令

				system("cls");
				cout << "请输入刚才所显示单词" << endl;
				starttimer = clock();
				char ch;
				char in_word[MAX_WORD_NUM + 1];
				cin.get(ch);
				cin.get(ch);
				int LetterNum;
				for (LetterNum = 0; (ch != '\n') && (LetterNum < MAX_WORD_NUM); LetterNum++)
				{
					in_word[LetterNum] = ch;
					cin.get(ch);
				}                   //读入本地的单词输入
				in_word[LetterNum] = '\0';
				if (strcomp(in_word, word[0]) == TRUE)
				{
					stoptimer = clock();
					float time = ((double)(stoptimer - starttimer)) / CLK_TCK;
					time = time + 1;
					cout << "等待系统判别........." << endl;
					ZeroMemory(sendbuf, BUF_SIZE);
					memcpy(sendbuf, &time, 4);
					send(client, sendbuf, strlen(sendbuf), 0);//把所用时间发过去

					ZeroMemory(recvebuf, BUF_SIZE);
					recv(client, recvebuf, BUF_SIZE, 0);//接收失败或者成功的确认
					if (recvebuf[0] == 'Y')
					{
						int cur_experience = (int)(get_num()*(INC_PLAYER_EXPER_RATIO / (time - 1))) * 2;//经验增长是平时的两倍
						change(PLAYER, get_num(), cur_experience);
					}
					else
					{
						int cur_experience = (int)(get_num()*(INC_PLAYER_EXPER_RATIO / (time - 1))) * (-2);
						change(PLAYER, get_num(), cur_experience);//失败后，会扣除原来的两倍经验
					}

					if (recvebuf[0] == 'Y')
						cout << "挑战成功" << endl;
					else
						cout << "挑战失败" << endl;
				}
				else
				{
					stoptimer = clock();
					float time = ((double)(stoptimer - starttimer)) / CLK_TCK;
					time = time + 1;

					cout << "输入错误" << endl;
					ZeroMemory(sendbuf, BUF_SIZE);//把输入错误的标志（N）发过去。
					sendbuf[0] = 'N';
					send(client, sendbuf, strlen(sendbuf), 0);
					ZeroMemory(recvebuf, BUF_SIZE);
					recv(client, recvebuf, BUF_SIZE, 0);//接收对方挑战是否成功的确认

					int cur_experience = (int)(get_num()*(INC_PLAYER_EXPER_RATIO / (time-1))) * (-2);
					change(PLAYER, get_num(), cur_experience);//失败后，会扣除原来的两倍经验
				}
				challange_lab = FALSE;
				for (int k = 0; k < WORD_NUM; k++)
				{
					delete [] word[k];
				}
				break;
			}
		}
		challange_lab = FALSE;
}