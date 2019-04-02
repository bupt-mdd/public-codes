#include<iostream>
#include<fstream>
#include<string>
#include<iomanip>
#include<windows.h>
#include"wordpool.h"
#include"individual.h"
#include"gamer.h"
#include"administration.h"
using namespace std;

int main()
{
	string player_inf = "player_information.txt";
	string adm_inf = "adm_information.txt";
	string e_question = "easy.txt";
	string m_question = "medium.txt";
	string d_question = "difficult.txt";

	gamer player;
	administrator set_question;
	word_pool e_pool, m_pool, d_pool;

	cout << "资源载入中......" << endl;
	e_pool.build_pool(EASY, e_question, m_question, d_question);
	m_pool.build_pool(MEDIUM, e_question, m_question, d_question);
	d_pool.build_pool(DIFFICULT, e_question, m_question, d_question);
	//建立三个不同的单词池。
	int command;
	char cmd_str[MAX_ARRAY_NUM];
	system("cls");
	cout << "********************************************************" << endl;
	cout << "*                        请选择操作                    *" << endl;
	cout << "*       1.玩游戏           2.出题            3.退出    *" << endl;
	cout << "*                                                      *" << endl;
	cout << "********************************************************" << endl;
	cin >> cmd_str;
	command = transfer_cmd(cmd_str);

	while (command != 3)
	{
		if (1 == command) 
			player.gamer_operation(PLAYER,player_inf,adm_inf ,e_pool ,m_pool ,d_pool);
		else if (2 == command)
			set_question.adm_operation(SET_QUE_MAN, player_inf, adm_inf, e_question, m_question,d_question,e_pool,m_pool,d_pool );

		system("cls");
		cout << "********************************************************" << endl;
		cout << "*                         请选择操作                   *" << endl;
		cout << "*       1.玩游戏           2.出题            3.退出    *" << endl;
		cout << "*                                                      *" << endl;
		cout << "********************************************************" << endl;
		cin >> cmd_str;
		command = transfer_cmd(cmd_str);
	}
	system("pause");
	return 0;
}