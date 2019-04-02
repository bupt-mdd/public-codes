#include<iostream>
#include<fstream>
#include<string>
#include<iomanip>
#include<windows.h>
#include<time.h>
#include"individual.h"
#include"wordpool.h"
#include"gamer.h"
using namespace std;

void gamer::run_game(int role, string player_inf, string adm_inf, word_pool e_pool, word_pool m_pool, word_pool d_pool, int pass_num)
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
	}
	char ch1;                   //按相应关卡从单词中随机取出单词
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

			cout << "请先用心记忆下面这个单词" << endl << word[i];
			Sleep(1000 * WAIT_TIME);
			system("cls");
			cout << "请输入刚才所显示单词" << endl;
			   
			    char ch;
			    cin.get(ch);
			    int LetterNum;
				for (LetterNum = 0; (ch != '\n') && (LetterNum<MAX_WORD_NUM); LetterNum++)
			    {
					in_word[LetterNum] = ch;
				    cin.get(ch);
			    }
				in_word[LetterNum] = '\0';

				cout << in_word;
			if (strcomp(in_word , word[i])==TRUE)
				i++;
			else
			{
				cout << "输入错误，闯关失败" << endl;
				fail_back = TRUE;
				break;
			}
		}
		if (i == (pass_num+1))
		{
			cout << "闯关成功。" << endl;
			pass_num++;

			stop_time = clock();

			duration = ((double)(stop_time - start_time)) / CLK_TCK;
			int  cur_experience = 0;
			cur_experience = (int)(pass_num*(INC_PLAYER_EXPER_RATIO / duration));

			if (pass_num > get_num())
			{
				change(PLAYER, player_inf, adm_inf, pass_num,cur_experience);
			}
		}
		char cmd_str[MAX_ARRAY_NUM];
		cout << "********************************************************" << endl;
		cout << "*                     请选择操作                       *" << endl;
		cout << "*  1.下一关           2.重玩本关           3.退出      *" << endl;
		cout << "********************************************************" << endl;
		cin >> cmd_str;
		in_command = transfer_cmd(cmd_str);

		while (in_command != 3&& in_command != 1 && in_command != 2)
		{
			system("cls");
			cout << "********************************************************" << endl;
			cout << "*                     请选择操作                       *" << endl;
			cout << "*  1.下一关           2.重玩本关           3.退出      *" << endl;
			cout << "********************************************************" << endl;
			cin >> cmd_str;
			in_command = transfer_cmd(cmd_str);
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
				//delete [] word;

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
				cout << "该关卡未解锁，只有通过本关才可以进入下一关" << endl;
				cout << "********************************************************" << endl;
				cout << "*                     请选择操作                       *" << endl;
				cout << "*  1.下一关           2.重玩本关           3.退出      *" << endl;
				cout << "********************************************************" << endl;
				cin >> cmd_str;
				in_command = transfer_cmd(cmd_str);

				while ((in_command != 2) && (in_command != 3))
				{
					system("cls");
					cout << "该关卡未解锁，只有通过本关才可以进入下一关" << endl;
					cout << "********************************************************" << endl;
					cout << "*                     请选择操作                       *" << endl;
					cout << "*  1.下一关           2.重玩本关           3.退出      *" << endl;
					cout << "********************************************************" << endl;
					cin >> cmd_str;
					in_command = transfer_cmd(cmd_str);

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

void gamer::play_game(int role, string player_inf, word_pool e_pool, word_pool m_pool, word_pool d_pool, string adm_inf)
{
	int command;
	char cmd_str[MAX_ARRAY_NUM];
    system("cls");
	cout << "********************************************************" << endl;
	cout << "*                     请选择操作                       *" << endl;
	cout << "*  1.重新开始         2.读取进度           3.退出      *" << endl;
	cout << "********************************************************" << endl;
	cin >> cmd_str;
	command = transfer_cmd(cmd_str);

	int pass_num = 0;
	while (command != 3)
	{
		switch (command)
		{
		case 1:                //从头开始进行游戏
			pass_num = 0;
			run_game(role,player_inf, adm_inf,e_pool,m_pool,d_pool, pass_num);
			break;
		case 2:
			pass_num = get_num();//按进度进行游戏
			run_game(role, player_inf, adm_inf, e_pool, m_pool, d_pool , pass_num);
			break;
		default: break;
		}
		system("cls");
		cout << "********************************************************" << endl;
		cout << "*                     请选择操作                       *" << endl;
		cout << "*  1.重新开始         2.读取进度           3.退出      *" << endl;
		cout << "********************************************************" << endl;
		cin >> cmd_str;
		command = transfer_cmd(cmd_str);

	}
}

void gamer::gamer_operation(int role, string player_inf, string  adm_inf, word_pool e_pool, word_pool m_pool, word_pool d_pool)
{
	int out_command;
	char cmd_str[MAX_ARRAY_NUM];
	system("cls");
	cout << "********************************************************" << endl;
	cout << "*                      请选择操作                      *" << endl;
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
				cout << "********************************************************" << endl;
				cout << "*                      请选择操作                      *" << endl;
				cout << "*       1游戏          2设置与查询           3.退出    *" << endl;
				cout << "********************************************************" << endl;
				cin >> cmd_str;
				in_command = transfer_cmd(cmd_str);

				while (in_command != 3)
				{
					switch (in_command)
					{
					case 1:play_game( role,player_inf,e_pool , m_pool , d_pool ,adm_inf); break;
					case 2:operate(role, player_inf, adm_inf); break;
					default:break;
					}
					system("cls");
					cout << "********************************************************" << endl;
					cout << "*                      请选择操作                      *" << endl;
					cout << "*       1游戏          2设置与查询           3.退出    *" << endl;
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

		system("cls");
	}
}
