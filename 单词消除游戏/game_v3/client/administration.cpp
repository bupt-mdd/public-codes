#include <Winsock2.h>
#include<iostream>
#include<fstream>
#include<string>
#include<iomanip>
#include<windows.h>
#include"mylib.h"
#include"individual.h"
#include"wordpool.h"
#include"administration.h"
#pragma comment(lib,"ws2_32.lib")
using namespace std;

void administrator::set_question(int role, 
	                            string e_question,string m_question,string d_question,
								word_pool e_pool,word_pool m_pool,word_pool d_pool)
{
	int command;
	system("cls");
	cout << "********************************************************" << endl;
	cout << "*                  请选择操作                          *" << endl;
	cout << "*     1.开始出题                2.出题结束（退出）     *" << endl;
	cout << "********************************************************" << endl;
	char cmd_str[MAX_ARRAY_NUM];
	char cmd;
	cin >> cmd_str;
	cmd = cmd_str[0];
	command = transfer_cmd(cmd);
	
	clock_t start_time, stop_time;
	double duration=0;

	while (command != 2)
	{
		int question_num = 0;
		string cur_word;
		if (1 == command)
		{
			int in_command = 1;
			fstream questionFile1(e_question, ios::out | ios::in);
			questionFile1.seekp(-1,ios::end);

			fstream questionFile2(m_question, ios::out | ios::in);
			questionFile2.seekp(-1,ios::end);

			fstream questionFile3(d_question, ios::out | ios::in);
			questionFile3.seekp(-1,ios::end);                          //打开三个不同难易的词库

			while (in_command != 2)
			{
				system("cls");
				if (1 == in_command)
				{
					start_time = clock();
					cout << "请输入想要增加的单词("<<MAX_WORD_NUM<<"个字母以内)" << endl;

					char cur_word[MAX_WORD_NUM + 1];
					char ch1,ch;
					cin.get(ch1);
					cin.get(ch);
					int LetterNum;
					for (LetterNum = 0; (ch != '\n') && (LetterNum<MAX_WORD_NUM); LetterNum++)
					{
						cur_word[LetterNum] = ch;
						cin.get(ch);
					}                      //对玩家输入的单词进行读入
					cur_word[LetterNum] = '\0';

					//通过单词字母个数来判断所属的字库。并进行添加
					if (LetterNum <= EASY)
					{
						int i = e_pool.insert_pool(cur_word);
						if (i == TRUE)
						{
							questionFile1 << setiosflags(ios::left) << setw(EASY) << setfill(' ') << cur_word << " "<<" ";
							cout << "出题成功" << endl;
							question_num++;
						}
						else
							cout << "出题失败"<<endl;
					}
					else if (LetterNum <= MEDIUM)
					{
						int i = m_pool.insert_pool(cur_word);
						if (i == TRUE)
						{
							questionFile2 << setiosflags(ios::left) << setw(MEDIUM) << setfill(' ') << cur_word << " " << " ";
							cout << "出题成功" << endl;
							question_num++;
						}
						else
							cout << "出题失败"<<endl;
					}
					else
					{
						int i = d_pool.insert_pool(cur_word);
						if (i == TRUE)
						{
							questionFile3 << setiosflags(ios::left) << setw(DIFFICULT) << setfill(' ') << cur_word << " " << " ";
							cout << "出题成功" << endl;
							question_num++;
						}
						else
							cout << "出题失败"<<endl;
					}

					stop_time = clock();
					duration = duration + ((double)(stop_time - start_time)) / CLK_TCK;//计算出题所用时间，为了下边计算经验
				}

				cout << "********************************************************" << endl;
				cout << "*                  请选择操作                          *" << endl;
				cout << "*       1.继续                          2.退出         *" << endl;
				cout << "********************************************************" << endl;
				cin >> cmd_str;
				cmd = cmd_str[0];
				in_command = transfer_cmd(cmd);
				
			}
			questionFile1 << " ";
			questionFile1.close();
			questionFile2 << " ";
			questionFile2.close();
			questionFile3 << " ";
			questionFile3.close();
			//出题结束，写入空格，因为我自定义的字库是通过空格的个数来判断文件结束。
			int cur_experience = 0;
			int word_num = get_num() + question_num;
			cur_experience = (int) (word_num+1) * (INC_SETQUE_EXPER_RATIO / duration);
			//计算经验（通过时间、目前所初的单词书以及出题者经验增长系数（INC_SETQUE_EXPER_RATIO）三个因素来实现）
			change(SET_QUE_MAN, get_num() + question_num,cur_experience);
		}
		system("cls");
		cout << "********************************************************" << endl;
		cout << "*                  请选择操作                          *" << endl;
		cout << "*     1.开始出题                2.出题结束（退出）     *" << endl;
		cout << "********************************************************" << endl;
		cin >> cmd_str;
		cmd = cmd_str[0];
		command = transfer_cmd(cmd);
	
	}
}

void administrator::adm_operation(int role,
	                             string e_question, string m_question, string d_question,
	                             word_pool e_pool, word_pool m_pool, word_pool d_pool)
{
	int out_command;
	system("cls");
	cout << "********************************************************" << endl;
	cout << "*                       请选择操作                     *" << endl;
	cout << "*       "<<REGISTER<<".注册           "<<LOGIN<<".登陆            3.退出      *" << endl;
	cout << "*                                                      *" << endl;
	cout << "********************************************************" << endl;
	char cmd_str[MAX_ARRAY_NUM];
	char cmd;
	cin >> cmd_str;
	cmd = cmd_str[0];
	out_command = transfer_cmd(cmd);

	while (out_command != 3)
	{
		switch (out_command)
		{
		case 1:
			int reg_back;
			reg_back = init_operate(REGISTER, role); break;//注册
		case 2:
		{
			int login_back = init_operate(LOGIN, role);
			if (login_back == TRUE)    //登陆成功后，进入相关操作
			{
				int in_command;
				system("cls");
				cout << "********************************************************" << endl;
				cout << "*                      请选择操作                      *" << endl;
				cout << "*       1出题          2设置与查询           3.退出    *" << endl;
				cout << "********************************************************" << endl;
				cin >> cmd_str;
				cmd = cmd_str[0];
				in_command = transfer_cmd(cmd);
				
				while (in_command != 3)
				{
					switch (in_command)
					{
					case 1:
						set_question(role, e_question,m_question,d_question,e_pool,m_pool,d_pool); 
					  break;

					case 2:operate(role); break;
					default:break;
					}
					system("cls");
					cout << "********************************************************" << endl;
					cout << "*                      请选择操作                      *" << endl;
					cout << "*       1出题          2设置与查询           3.退出    *" << endl;
					cout << "********************************************************" << endl;
					cin >> cmd_str;
					cmd = cmd_str[0];
					in_command = transfer_cmd(cmd);
				}
				if (in_command == 3)
				{
					int command;
					char recvebuf[BUF_SIZE], sendbuf[BUF_SIZE] = { "\0" };
					ZeroMemory(sendbuf, BUF_SIZE);       
					command = BACK;
					memcpy(sendbuf, &command, 4);
					int retVal = send(client, sendbuf, strlen(sendbuf), 0);//向服务器发送退出账户的请求
					
					ZeroMemory(recvebuf, BUF_SIZE);
					recv(client, recvebuf, BUF_SIZE, 0);// 接收服务器端的确认，
				}
			}

		}
		break;
		default: break;
		}
		
		cout << "********************************************************" << endl;
		cout << "*                       请选择操作                     *" << endl;
		cout << "*       " << REGISTER << ".注册           " << LOGIN << ".登陆            3.退出      *" << endl;
		cout << "*                                                      *" << endl;
		cout << "********************************************************" << endl;
		cin >> cmd_str;
		cmd = cmd_str[0];
		out_command = transfer_cmd(cmd);
		
	}
}
