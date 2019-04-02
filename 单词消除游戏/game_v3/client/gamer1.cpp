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

gamer::gamer()
	:whether(FALSE), challange_lab(FALSE)
{
	ZeroMemory(challange_account,PROPER_NUM);
	ZeroMemory(challange_name, PROPER_NUM);
}

gamer::~gamer()
{
}

void gamer::run_game(int role, word_pool e_pool, word_pool m_pool, word_pool d_pool, int pass_num)
{
	int fail_back = FALSE;

	char **word = NULL;
		word=new char*[pass_num+2];
	for (int i = 0; i < (pass_num + 2); i++)
	{
		word[i] = new char[MAX_WORD_NUM+1];
	}
	if (((pass_num+1) / 3) == 0)
	{
		e_pool.rand_word(word,0,pass_num);
	}
	else
	{
		e_pool.rand_word(word, 0 ,(pass_num + 1)/3-1);
		m_pool.rand_word(word, (pass_num + 1) / 3, 2*((pass_num + 1) / 3)-1);
		d_pool.rand_word(word, 2 * ((pass_num + 1) / 3), 3 * ((pass_num + 1) / 3) - 1);
		if ((3 * ((pass_num + 1) / 3) - 1) != pass_num )
			e_pool.rand_word(word, 3 * ((pass_num + 1) / 3), pass_num );
	}           //�����ֲ�ͬ�����׵ĵ��ʳ���ȡ����Ӧ�����ĵ���

	char ch1;
	cin.get(ch1);

	int in_command = 1;
	while (in_command == 1||in_command==2)
	{
		int i = 0;
		clock_t start_time, stop_time;
		double duration;
		char in_word[MAX_WORD_NUM+1];

		while (i <= pass_num)
		{
			system("cls");

			start_time = clock();

			cout << "�������ļ��������������" << endl << word[i];
			Sleep(1000 * WAIT_TIME);
			system("cls");
			cout << "������ղ�����ʾ����" << endl;
			 
			char ch;
			cin.get(ch);
			int LetterNum;
		    for (LetterNum = 0; (ch != '\n') && (LetterNum<MAX_WORD_NUM); LetterNum++)
		    {
				in_word[LetterNum] = ch;
				cin.get(ch);
			}
			in_word[LetterNum] = '\0';
		   if (strcomp(in_word, word[i]) == TRUE)
			{
				i++;
			}
			else
			{
				cout << "������󣬴���ʧ��" << endl;
				fail_back = TRUE;
				break;
			}
		}
		if (i == (pass_num+1))
		{
			cout << "���سɹ���" << endl;
			pass_num++;

			stop_time = clock();

			duration = ((double)(stop_time - start_time)) / CLK_TCK;
			int  cur_experience = 0;
			cur_experience = (int)(pass_num*(INC_PLAYER_EXPER_RATIO / duration));//����������ʽ

			if (pass_num > get_num())
			{
				change(PLAYER, pass_num,cur_experience);
			}
		}
		cout << "********************************************************" << endl;
		cout << "*                     ��ѡ�����                       *" << endl;
		cout << "*  1.��һ��           2.���汾��           3.�˳�      *" << endl;
		cout << "********************************************************" << endl;
		char cmd_str[MAX_ARRAY_NUM];
		char cmd;
		cin >> cmd_str;
		cmd = cmd_str[0];
		in_command = transfer_cmd(cmd);

		while (in_command != 3&& in_command != 1 && in_command != 2)
		{
			system("cls");
			cout << "********************************************************" << endl;
			cout << "*                     ��ѡ�����                       *" << endl;
			cout << "*  1.��һ��           2.���汾��           3.�˳�      *" << endl;
			cout << "********************************************************" << endl;
			cin >> cmd_str;
			cmd = cmd_str[0];
			in_command = transfer_cmd(cmd);
		}
		char ch1;
		cin.get(ch1);
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
				for (int i = 0; i < (pass_num + 1); i++)
				{
					delete [] word[i];
				}

				word = new char*[pass_num + 2];
				for (int i = 0; i < (pass_num + 2); i++)
				{
					word[i] = new char[MAX_WORD_NUM + 1];
				}

				if (((pass_num + 1) / 3) == 0)
				{
					e_pool.rand_word(word, 0, pass_num);
				}
				else
				{
					e_pool.rand_word(word, 0, (pass_num + 1) / 3 - 1);
					m_pool.rand_word(word, (pass_num + 1) / 3, 2 * ((pass_num + 1) / 3) - 1);
					d_pool.rand_word(word, 2 * ((pass_num + 1) / 3), 3 * ((pass_num + 1) / 3) - 1);
					if ((3 * ((pass_num + 1) / 3) - 1) != pass_num)
						e_pool.rand_word(word, 3 * ((pass_num + 1) / 3), pass_num);
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
				cmd = cmd_str[0];
				in_command = transfer_cmd(cmd);
				while ((in_command != 2) && (in_command != 3))
				{
					system("cls");
					cout << "�ùؿ�δ������ֻ��ͨ�����زſ��Խ�����һ��" << endl;
					cout << "********************************************************" << endl;
					cout << "*                     ��ѡ�����                       *" << endl;
					cout << "*  1.��һ��           2.���汾��           3.�˳�      *" << endl;
					cout << "********************************************************" << endl;
					cin >> cmd_str;
					cmd = cmd_str[0];
					in_command = transfer_cmd(cmd);
				}
				char ch1;
				cin.get(ch1);
			}
			break;
		case 2:
			if (fail_back == TRUE)
				fail_back = FALSE;
			break;
		default:break;
		}
	}

}

void gamer::play_game(int role,  word_pool e_pool, word_pool m_pool, word_pool d_pool)
{
	int command;
    system("cls");
	cout << "********************************************************" << endl;
	cout << "*                     ��ѡ�����                       *" << endl;
	cout << "*  1.���¿�ʼ         2.��ȡ����           3.�˳�      *" << endl;
	cout << "********************************************************" << endl;
	char cmd_str[MAX_ARRAY_NUM];
	char cmd;
	cin >> cmd_str;
	cmd = cmd_str[0];
	command = transfer_cmd(cmd);
	
	int pass_num = 0;
	while (command != 3)
	{
		switch (command)
		{
		case 1:
			pass_num = 0;
			run_game(role,e_pool,m_pool,d_pool, pass_num);//�����¿�ʼ����
			break;
		case 2:
			pass_num = get_num();
			run_game(role, e_pool, m_pool, d_pool , pass_num);//�ɶ�ȡ���Ƚ��д���
			break;
		default: break;
		}
		system("cls");
		cout << "********************************************************" << endl;
		cout << "*                     ��ѡ�����                       *" << endl;
		cout << "*  1.���¿�ʼ         2.��ȡ����           3.�˳�      *" << endl;
		cout << "********************************************************" << endl;
		cin >> cmd_str;
		cmd = cmd_str[0];
		command = transfer_cmd(cmd);
	}
}

void gamer::gamer_operation(int role,  word_pool e_pool, word_pool m_pool, word_pool d_pool)
{
	int out_command;
	system("cls");
	cout << "********************************************************" << endl;
	cout << "*                      ��ѡ�����                      *" << endl;
	cout << "*       " << REGISTER << ".ע��           " << LOGIN << ".��½            3.�˳�      *" << endl;
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
			reg_back = init_operate(REGISTER, role); //ע�ᴳ�����˺�
			
			break;
		case 2:
		{
			int login_back = init_operate(LOGIN, role);//��½�������˺�
			if (login_back == TRUE)
			{
				int in_command;
				cout << "********************************************************" << endl;
				cout << "*                      ��ѡ�����                      *" << endl;
				cout << "*      1������Ϸ       2������ս       3������ս       *" << endl;
				cout << "*      4��ѯ������                     5.�˳�          *" << endl;
				cout << "********************************************************" << endl;
				cin >> cmd_str;
				cmd = cmd_str[0];
				in_command = transfer_cmd(cmd);

				while (in_command != 5)
				{
					switch (in_command)
					{
					case 1:
						play_game( role,e_pool , m_pool , d_pool );
						system("cls"); 
						break;
					case 2:do_challange(e_pool, m_pool, d_pool);break;
					case 3:rec_challange(); break;
					case 4:
						operate(role); 
						system("cls");
						break;
					default:break;
					}
					cout << "********************************************************" << endl;
					cout << "*                      ��ѡ�����                      *" << endl;
					cout << "*      1������Ϸ       2������ս       3������ս       *" << endl;
					cout << "*      4��ѯ������                     5.�˳�          *" << endl;
					cout << "********************************************************" << endl;
					cin >> cmd_str;
					cmd = cmd_str[0];
					in_command = transfer_cmd(cmd);
				}
				if (in_command == 5)
				{
					int command;
					char recvebuf[BUF_SIZE], sendbuf[BUF_SIZE] = { "\0" };
					ZeroMemory(sendbuf, BUF_SIZE);       
					command = BACK;
					memcpy(sendbuf, &command, 4);
					int retVal = send(client, sendbuf, strlen(sendbuf), 0);//������������˳����˺�����
					// ���շ������˵�ȷ�ϣ�
					ZeroMemory(recvebuf, BUF_SIZE);
					recv(client, recvebuf, BUF_SIZE, 0);
				}
			}
		}
		break;
		default: break;
		}
		
		cout << "********************************************************" << endl;
		cout << "*                       ��ѡ�����                     *" << endl;
		cout << "*       " << REGISTER << ".ע��           " << LOGIN << ".��½            3.�˳�      *" << endl;
		cout << "*                                                      *" << endl;
		cout << "********************************************************" << endl;
		cin >> cmd_str;
		cmd = cmd_str[0];
		out_command = transfer_cmd(cmd);
		system("cls");
	}
}
