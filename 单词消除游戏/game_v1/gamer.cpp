#include<iostream>
#include<fstream>
#include<string>
#include<iomanip>
#include<windows.h>
#include"individual.h"
#include"gamer.h"
using namespace std;

void gamer::run_game(int role,string player_inf, string adm_inf, string question, int pass_num)
{
	int fail_back = FALSE;
	string word[WORD_NUM];

	ifstream questionFile(question);
	for (int i = 0; i <= pass_num; i++)
	{
		for (int j = 0; j < WORD_NUM&&!questionFile.eof(); j++)
		{
			questionFile >> word[j];
		}
	}
	int in_command = 1;
	while (!questionFile.eof() && (in_command == 1||in_command==2))
	{
		int i = 0;
		string in_word;
		while (i < WORD_NUM)
		{
			system("cls");
			cout << "�������ļ��������������" << endl << word[i];
			Sleep(1000 * WAIT_TIME);
			system("cls");
			cout << "������ղ�����ʾ����" << endl;
			cin >> in_word;
			if (in_word == word[i])
				i++;
			else
			{
				cout << "������󣬴���ʧ��" << endl;
				fail_back = TRUE;
				break;
			}
		}
		if (i == WORD_NUM)
		{
			cout << "���سɹ���" << endl;
			pass_num++;
			if (pass_num > get_num())
			{
				change_que_or_passnum(PLAYER, player_inf, adm_inf, pass_num);
			}
		}
		char cmd_str[MAX_ARRAY_NUM];
		cout << "********************************************************" << endl;
		cout << "*                     ��ѡ�����                       *" << endl;
		cout << "*  1.��һ��           2.���汾��           3.�˳�      *" << endl;
		cout << "********************************************************" << endl;
		cin >> cmd_str;
		in_command = transfer_cmd(cmd_str);
		
		while (in_command != 3&& in_command != 1 && in_command != 2)
		{
			system("cls");
			cout << "********************************************************" << endl;
			cout << "*                     ��ѡ�����                       *" << endl;
			cout << "*  1.��һ��           2.���汾��           3.�˳�      *" << endl;
			cout << "********************************************************" << endl;
			cin >> cmd_str;
			in_command = transfer_cmd(cmd_str);
			
		}
		switch (in_command)
		{
		case 1:
			if (fail_back == TRUE)
			{
				pass_num++;
				fail_back = FALSE;
			}

			if (pass_num <= get_num())
			{
				for (int j = 0; j < WORD_NUM&&!questionFile.eof(); j++)
				{
					questionFile >> word[j];
				}
			}
			else if (pass_num > get_num())
			{
				pass_num--;
				system("cls");
				cout << "�ùؿ�δ������ֻ��ͨ�����زſ��Խ�����һ��" << endl;
				cout << "********************************************************" << endl;
				cout << "*                     ��ѡ�����                       *" << endl;
				cout << "*  1.��һ��           2.���汾��           3.�˳�      *" << endl;
				cout << "********************************************************" << endl;
				cin >> cmd_str;
				in_command = transfer_cmd(cmd_str);

				while ((in_command != 2) && (in_command != 3))
				{
					system("cls");
					cout << "�ùؿ�δ������ֻ��ͨ�����زſ��Խ�����һ��" << endl;
					cout << "********************************************************" << endl;
					cout << "*                     ��ѡ�����                       *" << endl;
					cout << "*  1.��һ��           2.���汾��           3.�˳�      *" << endl;
					cout << "********************************************************" << endl;
					cin >> cmd_str;
					in_command = transfer_cmd(cmd_str);
					
				}
			}
			break;
		case 2:
			if (fail_back == 1)
				fail_back = FALSE;
			break;
		default:break;
		}
	}
	if (questionFile.eof())
		cout << "��ϲͨ��ȫ��" << endl;
	questionFile.close();
}

void gamer::play_game(int role, string player_inf, string question, string adm_inf )
{
	char cmd_str[MAX_ARRAY_NUM];
	int command;
    system("cls");
	cout << "********************************************************" << endl;
	cout << "*                     ��ѡ�����                       *" << endl;
	cout << "*  1.���¿�ʼ         2.��ȡ����           3.�˳�      *" << endl;
	cout << "********************************************************" << endl;
	cin >> cmd_str;
	command = transfer_cmd(cmd_str);
	
	int pass_num = 0;
	while (command != 3)
	{
		switch (command)
		{
		case 1:
			pass_num = 0;
			run_game(role,player_inf, question, adm_inf, pass_num);
			break;
		case 2:
			pass_num = get_num();
			run_game(role,player_inf, question, adm_inf,pass_num);
			break;
		default: break;
		}
		system("cls");
		cout << "********************************************************" << endl;
		cout << "*                     ��ѡ�����                       *" << endl;
		cout << "*  1.���¿�ʼ         2.��ȡ����           3.�˳�      *" << endl;
		cout << "********************************************************" << endl;
		cin >> cmd_str;
		command = transfer_cmd(cmd_str);
	}
}

void gamer::gamer_operation(int role, string player_inf, string  adm_inf, string question)
{
	char cmd_str[MAX_ARRAY_NUM];
	int out_command;
	system("cls");
	cout << "********************************************************" << endl;
	cout << "*                      ��ѡ�����                      *" << endl;
	cout << "*       1.ע��           2.��½            3.�˳�      *" << endl;
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
				cout << "********************************************************" << endl;
				cout << "*                      ��ѡ�����                      *" << endl;
				cout << "*       1��Ϸ          2�������ѯ           3.�˳�    *" << endl;
				cout << "********************************************************" << endl;
				cin >> cmd_str;
				in_command = transfer_cmd(cmd_str);
				
				while (in_command != 3)
				{
					switch (in_command)
					{
					case 1:play_game( role,player_inf,adm_inf, question); break;
					case 2:operate(role, player_inf, adm_inf); break;
					default:break;
					}
					system("cls");
					cout << "********************************************************" << endl;
					cout << "*                      ��ѡ�����                      *" << endl;
					cout << "*       1��Ϸ          2�������ѯ           3.�˳�    *" << endl;
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
		cout << "*                       ��ѡ�����                     *" << endl;
		cout << "*       1.ע��           2.��½            3.�˳�      *" << endl;
		cout << "*                                                      *" << endl;
		cout << "********************************************************" << endl;
		cin >> cmd_str;
		out_command = transfer_cmd(cmd_str);
		system("cls");
	}
}
