#include<iostream>
#include<fstream>
#include<string>
#include<iomanip>
#include<windows.h>
#include"individual.h"
#include"administration.h"
using namespace std;

void administrator::set_question(int role, string player_inf, string  adm_inf, string question)
{
	char cmd_str[MAX_ARRAY_NUM];
	int command;
	system("cls");
	cout << "********************************************************" << endl;
	cout << "*                  请选择操作                          *" << endl;
	cout << "*     1.开始出题                2.出题结束（退出）     *" << endl;
	cout << "********************************************************" << endl;
	cin >> cmd_str;
	command = transfer_cmd(cmd_str);

	ofstream questionFile(question, ios::out | ios::app);
	questionFile.seekp(ios::end);
	while (command != 2)
	{
		int question_num = 0;
		string cur_word;
		if (1 == command)
		{
			questionFile << endl;
			int in_command = 1;
			while (in_command != 2)
			{
				system("cls");
				if (1 == in_command)
				{
					cout << "请输入想要增加的单词(20个字母以内，无空格)" << endl;
					cin >> cur_word;
					questionFile << setiosflags(ios::right) << setw(20) << setfill(' ') << cur_word << " ";
					cout << "出题成功" << endl;
					question_num++;
					if (question_num%WORD_NUM == 0)
						questionFile << endl;
				}
				cout << "********************************************************" << endl;
				cout << "*                  请选择操作                          *" << endl;
				cout << "*       1.继续                          2.退出         *" << endl;
				cout << "********************************************************" << endl;
				cin >> cmd_str;
				in_command = transfer_cmd(cmd_str);
	
			}
			change_que_or_passnum(SET_QUE_MAN, player_inf, adm_inf, get_num() + question_num);
		}
		system("cls");
		cout << "********************************************************" << endl;
		cout << "*                  请选择操作                          *" << endl;
		cout << "*     1.开始出题                2.出题结束（退出）     *" << endl;
		cout << "********************************************************" << endl;
		cin >> cmd_str;
		command = transfer_cmd(cmd_str);
	}
	questionFile.close();
}

void administrator::adm_operation(int role, string player_inf, string  adm_inf, string question)
{
	char cmd_str[MAX_ARRAY_NUM];
	int out_command;
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
					case 1:set_question(role, player_inf, adm_inf, question); break;
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
		cout << "********************************************************" << endl;
		cout << "*                       请选择操作                     *" << endl;
		cout << "*       1.注册           2.登陆            3.退出      *" << endl;
		cout << "*                                                      *" << endl;
		cout << "********************************************************" << endl;
		cin >> cmd_str;
		out_command = transfer_cmd(cmd_str);
	}
}
