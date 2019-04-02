#include<iostream>
#include<fstream>
#include<string>
#include<iomanip>
#include<windows.h>
#include"individual.h"
using namespace std;

void individual::merge(individual *&Arrayptr, individual *&Arrayptr_copy, int left, int q, int right)
{
	int n = right - left + 1, i, j, num;
	int num1 = q - left + 1;
	int num2 = right - q;
	for (i = 0, j = 0, num = 0; (i<num1) && (j<num2); num++)
	{
		if (Arrayptr[left + i].sort_standard > Arrayptr[q + 1 + j].sort_standard)
		{
			Arrayptr_copy[left + num] = Arrayptr[left + i];
			i++;
		}
		else
		{
			Arrayptr_copy[left + num] = Arrayptr[q + 1 + j];
			j++;
		}
	}
	if (i == num1)
		for (; j<num2; j++, num++)
			Arrayptr_copy[left + num] = Arrayptr[q + 1 + j];
	else
		for (; i<num1; i++, num++)
			Arrayptr_copy[left + num] = Arrayptr[left + i];
}

void individual::merge_pass(individual *&Arrayptr, individual *&Arrayptr_1, int s, int num)
{
	int i = 0;
	while ((i + 2 * s) <= num)               //（i+2*s-1）<num 
	{
		merge(Arrayptr, Arrayptr_1, i, i + s - 1, i + 2 * s - 1);
		i = i + (2 * s);
	}
	if (i + s<num)
		merge(Arrayptr, Arrayptr_1, i, i + s - 1, num - 1);
	else
		for (int j = i; j <= num - 1; j++)
			Arrayptr_1[j] = Arrayptr[j];
}

void individual::merge_sort(individual *&Arrayptr, int num)
{
	individual *Arrayptr_1 = new individual[num];
	int s = 1;
	while (s<num)
	{
		merge_pass(Arrayptr, Arrayptr_1, s, num);
		s += s;
		merge_pass(Arrayptr_1, Arrayptr, s, num);
		s += s;
	}
	delete[] Arrayptr_1;
}
//合并排序实现玩家信息按属性排序
void individual::show_result(individual *Arrayptr, int num)
{
	for (int i = 0; i < num; i++)
	{
		cout << "第" << setw(3) << setiosflags(ios::left) << i + 1 << "名：" << endl;
		cout << "账号为：" << " " << Arrayptr[i].game_account
			 << "玩家名为:" << " " << Arrayptr[i].user_name
			 << "等级为:" << " " << Arrayptr[i].user_rank
			 << "经验为:" << " " << Arrayptr[i].user_experience
			 << "出题数或者闯关数:" << " " << Arrayptr[i].que_or_passnum<<endl;
	}
}//输出显示玩家的信息。

void individual::sort( string player_inf, string  adm_inf)
{
	individual *Arrayptr = new individual[MAX_ARRAY_NUM];
	int out_command;
	char cmd_str[MAX_ARRAY_NUM];
	system("cls");
	cout << "********************************************************" << endl;
	cout << "*                   请选择排序对象                     *" << endl;
	cout << "*         "<<PLAYER<<"玩家          "<<SET_MAN<<"出题者        3退出　        *" << endl;
	cout << "********************************************************" << endl;
	cin >> cmd_str;
	out_command = transfer_cmd(cmd_str);

	while (out_command != 3)
	{
		int i = 0;
		if (out_command == PLAYER)
		{
			ifstream AccountFile1(player_inf);
			while (!AccountFile1.eof() && out_command != 3)
			{
				AccountFile1 >> Arrayptr[i].game_account
					>> Arrayptr[i].user_name
					>> Arrayptr[i].user_password
					>> Arrayptr[i].user_rank
					>> Arrayptr[i].user_experience
					>> Arrayptr[i].que_or_passnum;
				i++;
			}
			AccountFile1.close();
		}
		else if(out_command==SET_MAN)
		{
			ifstream AccountFile1(adm_inf);
			while (!AccountFile1.eof() && out_command != 3)
			{
				AccountFile1 >> Arrayptr[i].game_account
					>> Arrayptr[i].user_name
					>> Arrayptr[i].user_password
					>> Arrayptr[i].user_rank
					>> Arrayptr[i].user_experience
					>> Arrayptr[i].que_or_passnum;
				i++;
			}
			AccountFile1.close();
		}
	
		int num = i;
		int in_command;
		system("cls");
		cout << "********************************************************" << endl;
		cout << "*                   请选择排序操作                     *" << endl;
		cout << "*         1按等级                 2按出题数（过关数）  *" << endl;
		cout << "*         3按经验                 4退出                *" << endl;
		cout << "********************************************************" << endl;
		cin >> cmd_str;
		in_command = transfer_cmd(cmd_str);

		system("cls");
		while (in_command != 4&&out_command!=3)
		{
			switch (in_command)
			{
			case 1:
				for (int i = 0; i < num; i++)
				{
					Arrayptr[i].sort_standard = Arrayptr[i].user_rank;
				}
				merge_sort(Arrayptr, num);
				system("cls");
				show_result(Arrayptr, num);
				break;
			case 2:
				for (int i = 0; i < num; i++)
				{
					Arrayptr[i].sort_standard = Arrayptr[i].que_or_passnum;
				}
				merge_sort(Arrayptr, num);
				system("cls");
				show_result(Arrayptr, num);
				break;
			case 3:
				for (int i = 0; i < num; i++)
				{
					Arrayptr[i].sort_standard = Arrayptr[i].user_experience;
				}
				merge_sort(Arrayptr, num);
				system("cls");
				show_result(Arrayptr, num);
				break;
			default:break;
			}
			cout << "********************************************************" << endl;
			cout << "*                   请选择排序操作                     *" << endl;
			cout << "*         1按等级                 2按出题数（过关数）  *" << endl;
			cout << "*         3按经验                 4退出                *" << endl;
			cout << "********************************************************" << endl;
			cin >> cmd_str;
			in_command = transfer_cmd(cmd_str);

			system("cls");
		}
		system("cls");
		cout << "********************************************************" << endl;
		cout << "*                   请选择排序对象                     *" << endl;
		cout << "*         " << PLAYER << "玩家          " << SET_MAN << "出题者        3退出　        *" << endl;
		cout << "********************************************************" << endl;
		cin >> cmd_str;
		out_command = transfer_cmd(cmd_str);

		system("cls");
	}
}

void individual::operate(int role, string player_inf, string  adm_inf)
{
	int command;
	char cmd_str[MAX_ARRAY_NUM];
	system("cls");
	cout << "********************************************************" << endl;
	cout << "*                    请选择操作                        *" << endl;
	cout << "*    1查询所有成员     2按属性查询      3修改密码      *" << endl;
	cout << "*    4修改姓名         5排序输出        6退出          *" << endl;
	cout << "********************************************************" << endl;
	cin >> cmd_str;
	command = transfer_cmd(cmd_str);

	while (command != 6)
	{
		system("cls");
		switch (command)
		{
		case 1:
			search_All_individual(role, player_inf, adm_inf);
			break;
		case 2:
			search_individual(role, player_inf, adm_inf);
			break;
		case 3:
			system("cls");
			if (role == SET_QUE_MAN)
				change_password(adm_inf);
			else
				change_password(player_inf);
			break;
		case 4:
			if (role == SET_QUE_MAN)
				change_username(adm_inf);
			else
				change_username(player_inf);
			break;
		case 5:
			sort(player_inf, adm_inf);
				break;
		default:break;
		}
		cout << "********************************************************" << endl;
		cout << "*                    请选择操作                        *" << endl;
		cout << "*    1查询所有成员     2按属性查询      3修改密码      *" << endl;
		cout << "*    4修改姓名         5排序输出        6退出          *" << endl;
		cout << "********************************************************" << endl;
		cin >> cmd_str;
		command = transfer_cmd(cmd_str);
	}

}

int individual::init_operate(int command, int role, string player_inf, string adm_inf)//通过该函数调用相应的登陆与注册函数
{
	if (role == SET_QUE_MAN)
	{
		if (REGISTER == command)
			return user_login(adm_inf);
		else
			return user_register(adm_inf);
	}
	else
	{
		if (REGISTER == command)
			return user_login(player_inf);
		else
			return user_register(player_inf);
	}
}
