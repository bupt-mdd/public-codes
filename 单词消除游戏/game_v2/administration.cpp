#include<iostream>
#include<fstream>
#include<string>
#include<iomanip>
#include<windows.h>
#include"individual.h"
#include"wordpool.h"
#include"administration.h"
using namespace std;

void administrator::set_question(int role, 
	                            string player_inf, string  adm_inf, 
	                            string e_question,string m_question,string d_question,
								word_pool e_pool,word_pool m_pool,word_pool d_pool)
{
	int command;
	char cmd_str[MAX_ARRAY_NUM];
	system("cls");
	cout << "********************************************************" << endl;
	cout << "*                  请选择操作                          *" << endl;
	cout << "*     1.开始出题                2.出题结束（退出）     *" << endl;
	cout << "********************************************************" << endl;
	cin >> cmd_str;
	command = transfer_cmd(cmd_str);

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
			questionFile3.seekp(-1,ios::end);
			//打开不同难易的三个单词库
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
					}
					cur_word[LetterNum] = '\0';

					if (LetterNum <= EASY)
					{
						int i = e_pool.insert_pool(cur_word);
						if (i == TRUE)
						{
							questionFile1 << setiosflags(ios::left) << setw(EASY) << setfill(' ') << cur_word << " "<<" ";
							cout << "出题成功" << endl;
							question_num++;//出题成功后，将单词插入单词池的同时，也将其写入不同难易的词库中
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
							question_num++;//出题成功后，将单词插入单词池的同时，也将其写入不同难易的词库中
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
						}//出题成功后，将单词插入单词池的同时，也将其写入不同难易的词库中
						else
							cout << "出题失败"<<endl;
					}

					stop_time = clock();
					duration = duration + ((double)(stop_time - start_time)) / CLK_TCK;
				}

				cout << "********************************************************" << endl;
				cout << "*                  请选择操作                          *" << endl;
				cout << "*       1.继续                          2.退出         *" << endl;
				cout << "********************************************************" << endl;
				cin >> cmd_str;
				in_command = transfer_cmd(cmd_str);
			}
			questionFile1 << " ";
			questionFile1.close();
			questionFile2 << " ";
			questionFile2.close();
			questionFile3 << " ";
			questionFile3.close();

			int cur_experience = 0;
			int word_num = get_num() + question_num;
			cur_experience = (int) (word_num+1) * (INC_SETQUE_EXPER_RATIO / duration);
			
			change(SET_QUE_MAN, player_inf, adm_inf, get_num() + question_num,cur_experience);
		}
		system("cls");
		cout << "********************************************************" << endl;
		cout << "*                  请选择操作                          *" << endl;
		cout << "*     1.开始出题                2.出题结束（退出）     *" << endl;
		cout << "********************************************************" << endl;
		cin >> cmd_str;
		command = transfer_cmd(cmd_str);
	}
}

void administrator::adm_operation(int role,
	                             string player_inf, string  adm_inf,
	                             string e_question, string m_question, string d_question,
	                             word_pool e_pool, word_pool m_pool, word_pool d_pool)
{
	int out_command;
	char cmd_str[MAX_ARRAY_NUM];
	system("cls");
	cout << "********************************************************" << endl;
	cout << "*                       请选择操作                     *" << endl;
	cout << "*       1.注册           2.登陆            3.退出      *" << endl;
	cout << "*                                                      *" << endl;
	cout << "********************************************************" << endl;
	cin >> cmd_str;
	out_command = transfer_cmd(cmd_str);

	while (out_command != 3)
	{
		switch (out_command)
		{
		case 1:
			int reg_back;
			reg_back = init_operate(1, role, player_inf, adm_inf); break;
		case 2:
		{
			int login_back = init_operate(2, role, player_inf, adm_inf);
			if (login_back == TRUE)
			{
				int in_command;
				system("cls");
				cout << "********************************************************" << endl;
				cout << "*                      请选择操作                      *" << endl;
				cout << "*       1出题          2设置与查询           3.退出    *" << endl;
				cout << "********************************************************" << endl;
				cin >> cmd_str;
				in_command = transfer_cmd(cmd_str);

				while (in_command != 3)
				{
					switch (in_command)
					{
					case 1:
						set_question(role, player_inf, adm_inf, e_question,m_question,d_question,e_pool,m_pool,d_pool); 
					  break;

					case 2:operate(role, player_inf, adm_inf); break;
					default:break;
					}
					system("cls");
					cout << "********************************************************" << endl;
					cout << "*                      请选择操作                      *" << endl;
					cout << "*       1出题          2设置与查询           3.退出    *" << endl;
					cout << "********************************************************" << endl;
					cin >> cmd_str;
					in_command = transfer_cmd(cmd_str);

				}
			}

		}
		break;
		default: break;
		}
		system("cls");
		cout << "********************************************************" << endl;
		cout << "*                       请选择操作                     *" << endl;
		cout << "*       1.注册           2.登陆            3.退出      *" << endl;
		cout << "*                                                      *" << endl;
		cout << "********************************************************" << endl;
		cin >> cmd_str;
		out_command = transfer_cmd(cmd_str);
	}
}
