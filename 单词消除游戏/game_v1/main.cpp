#include<iostream>
#include<fstream>
#include<string>
#include<iomanip>
#include<windows.h>
#include"individual.h"
#include"gamer.h"
#include"administration.h"
using namespace std;

int main()
{
	string player_inf, adm_inf, question;

	player_inf = "player_information.txt";
	adm_inf = "adm_information.txt";
	question = "question.txt";

	gamer player;
	administrator set_question;

	char cmd_str[MAX_ARRAY_NUM];
	int command;
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
			player.gamer_operation(PLAYER,player_inf,adm_inf, question);
		else if (2 == command)
			set_question.adm_operation(SET_QUE_MAN,player_inf, adm_inf, question);
		//system("cls");
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