#include<iostream>
#include<fstream>
#include<string>
#include<iomanip>
#include<windows.h>
#include"individual.h"
using namespace std;

individual::individual()
	:user_experience(0), sort_standard(0) ,user_rank(0), que_or_passnum(0)
{
	user_name = { "\0" };
	game_account = { "\0" };
	user_password = { "\0" };
}

individual::individual(string& account, string& name, string& password,
	                   int experience, int standard, int rank, int num)
	       :game_account(account), user_name(name), user_password(password),
        	user_experience(experience), sort_standard(standard),
	        user_rank(rank),que_or_passnum(que_or_passnum)
{
}

individual::individual(const individual& I)
	       :game_account(I.game_account), user_name(I.user_name), user_password(I.user_password),
	        user_experience(I.user_experience), sort_standard(I.sort_standard),
	        user_rank(I.user_rank),que_or_passnum(I.que_or_passnum)
{
}

void individual::change_username(string cur_inf)//�޸��������
{
	string copy_account, copy_name, copy_code;
	int copy_rank, copy_experience, copy_num;
	fstream AccountFile(cur_inf, ios::in | ios::out);
	AccountFile.seekg(ios::beg);

	AccountFile >> copy_account;
	while (!AccountFile.eof() && (copy_account != game_account))
	{
		AccountFile >> copy_name
			>> copy_code
			>> copy_rank
			>> copy_experience
			>> copy_num;
		AccountFile >> copy_account;
	}
	streampos position = AccountFile.tellg();
	if (copy_account == game_account)
	{
		string new_name;
		cout << "�������µ��û���";
		cin >> new_name;
		user_name = new_name;
		AccountFile.seekp(position);
		AccountFile << " " << setw(PROPER_NUM) << setiosflags(ios::right) << setfill(' ') << user_name;
		AccountFile.close();
		cout << "�����޸ĳɹ�" << endl;
	}
	else
		cout << "ϵͳ���ִ���" << endl;
}

void individual::change_password(string cur_inf)//�޸�����
{
	string copy_account, copy_name, copy_code;
	int copy_rank, copy_experience, copy_num;
	fstream AccountFile(cur_inf, ios::in | ios::out);
	AccountFile.seekg(ios::beg);

	AccountFile >> copy_account;
	while (!AccountFile.eof() && (copy_account != game_account))
	{
		AccountFile >> copy_name
			>> copy_code
			>> copy_rank
			>> copy_experience
			>> copy_num;
		AccountFile >> copy_account;
	}
	streampos position = AccountFile.tellg();
	string old_password, new_password1, new_password2;
	cout << "������ɵ�����";
	cin >> old_password;
	cout << "�������µ�����";
	cin >> new_password1;
	cout << "�������µ�����";
	cin >> new_password2;
	if (new_password1 == new_password2&&old_password == user_password)
	{
		user_password = new_password1;
		AccountFile.seekp(position);
		AccountFile << " " << setw(PROPER_NUM) << setiosflags(ios::right) << setfill(' ') << user_name
			<< " " << setw(PROPER_NUM) << setiosflags(ios::right) << setfill(' ') << user_password;
		AccountFile.close();
		cout << "�����޸ĳɹ�" << endl;
	}
	else
	{
		cout << "�����޸�ʧ�ܡ�" << endl;
	}
}

int individual::user_register(string cur_inf)//��ҵ�½
{
	system("cls");
	string account, old_account = { "\0" };
	cout << "������ע����Ϸ�˺�";
	cin >> account;

	ifstream AccountFile1(cur_inf, ios::in);
	char other_inf[MAXNUM_STR];
	while (!AccountFile1.eof() && (old_account != account))
	{
		AccountFile1 >> old_account;
		AccountFile1.getline(other_inf, MAXNUM_STR);
	}
	if (old_account != account)
	{
		game_account = account;
		cout << "�������û�����";
		string name;
		cin >> name;
		user_name = name;
		cout << "����������";
		string code;
		cin >> code;
		user_password = code;
		cout << "ע��ɹ���" << endl;
		AccountFile1.close();

		ofstream AccountFile2(cur_inf, ios::app | ios::out);
		AccountFile2
			<< endl << setw(PROPER_NUM) << setiosflags(ios::right) << game_account
			<< " " << setw(PROPER_NUM) << setiosflags(ios::right) << user_name
			<< " " << setw(PROPER_NUM) << setiosflags(ios::right) << user_password
			<< " " << setw(PROPER_NUM) << setiosflags(ios::right) << user_rank
			<< " " << setw(PROPER_NUM) << setiosflags(ios::right) << user_experience
			<< " " << setw(PROPER_NUM) << setiosflags(ios::right) << que_or_passnum;
		AccountFile2.close();
		return TRUE;
	}
	else
	{
		cout << "���˺��Ѿ�����" << endl;
		return FALSE;
	}
}

int individual::user_login(string cur_inf)//���ע��
{
	system("cls");
	string account;
	int copy_rank, copy_experience, copy_num;
	cout << "��������Ϸ�˺�";
	cin >> account;
	string code;
	cout << "����������";
	cin >> code;
	ifstream AccountFile1(cur_inf);
	string copy_account, copy_name, copy_code;
	AccountFile1 >> copy_account
		>> copy_name
		>> copy_code
		>> copy_rank
		>> copy_experience
		>> copy_num;
	while (!AccountFile1.eof() && (copy_account != account))
	{
		AccountFile1 >> copy_account
			>> copy_name
			>> copy_code
			>> copy_rank
			>> copy_experience
			>> copy_num;
	}
	if ((copy_code == code) && (copy_account == account))
	{
		game_account = copy_account;
		user_name = copy_name;
		user_password = copy_code;
		user_rank = copy_rank;
		user_experience = copy_experience;
		que_or_passnum = copy_num;
		cout << "��½�ɹ�" << endl;
		AccountFile1.close();
		return TRUE;
	}
	else
	{
		cout << "�˺Ż��������" << endl;
		AccountFile1.close();
		return FALSE;
	}
}

void individual::change_que_or_passnum(int role, string player_inf, string adm_inf, int num)
{
	if (role == PLAYER)
	{
		string copy_account, copy_name, copy_code;
		int copy_rank, copy_experience, copy_num;
		fstream AccountFile(player_inf, ios::in | ios::out);
		AccountFile.seekg(ios::beg);

		AccountFile >> copy_account;
		while (!AccountFile.eof() && (copy_account != game_account))
		{
			AccountFile >> copy_name
				>> copy_code
				>> copy_rank
				>> copy_experience
				>> copy_num;
			AccountFile >> copy_account;
		}
		que_or_passnum = num;
		streampos position = AccountFile.tellg();
		AccountFile.seekp(position);
		AccountFile << " " << setw(PROPER_NUM) << setiosflags(ios::right) << setfill(' ') << user_name
			<< " " << setw(PROPER_NUM) << setiosflags(ios::right) << setfill(' ') << user_password
			<< " " << setw(PROPER_NUM) << setiosflags(ios::right) << setfill(' ') << user_rank
			<< " " << setw(PROPER_NUM) << setiosflags(ios::right) << setfill(' ') << user_experience
			<< " " << setw(PROPER_NUM) << setiosflags(ios::right) << setfill(' ') << que_or_passnum;
		AccountFile.close();
	}
	else
	{
		string copy_account, copy_name, copy_code;
		int copy_rank, copy_experience, copy_num;
		fstream AccountFile(adm_inf, ios::in | ios::out);
		AccountFile.seekg(ios::beg);

		AccountFile >> copy_account;
		while (!AccountFile.eof() && (copy_account != game_account))
		{
			AccountFile >> copy_name
				>> copy_code
				>> copy_rank
				>> copy_experience
				>> copy_num;
			AccountFile >> copy_account;
		}
		que_or_passnum = num;
		streampos position = AccountFile.tellg();
		AccountFile.seekp(position);
		AccountFile << " " << setw(PROPER_NUM) << setiosflags(ios::right) << setfill(' ') << user_name
			<< " " << setw(PROPER_NUM) << setiosflags(ios::right) << setfill(' ') << user_password
			<< " " << setw(PROPER_NUM) << setiosflags(ios::right) << setfill(' ') << user_rank
			<< " " << setw(PROPER_NUM) << setiosflags(ios::right) << setfill(' ') << user_experience
			<< " " << setw(PROPER_NUM) << setiosflags(ios::right) << setfill(' ') << que_or_passnum;
		AccountFile.close();
	}
}

void individual::search_All_individual(int role, string player_inf, string  adm_inf)//��ѯ���е������Ϣ
{
	string copy_account, copy_name, copy_code;
	int copy_rank, copy_experience, copy_num;
	cout << "�������˺���Ϣ" << endl;

	cout << setw(PROPER_NUM) << setiosflags(ios::right) << setfill(' ') << "�˺�Ϊ��"
		<< setw(PROPER_NUM) << setiosflags(ios::right) << setfill(' ') << "�����Ϊ:"
		<< setw(PROPER_NUM / 2) << setiosflags(ios::right) << setfill(' ') << "�ȼ�Ϊ:"
		<< setw(PROPER_NUM / 2) << setiosflags(ios::right) << setfill(' ') << "����Ϊ:"
		<< setw(PROPER_NUM / 2) << setiosflags(ios::right) << setfill(' ') << "������:" << endl;

	ifstream AccountFile1(player_inf);
	while (!AccountFile1.eof())
	{
		AccountFile1 >> copy_account
			>> copy_name
			>> copy_code
			>> copy_rank
			>> copy_experience
			>> copy_num;

		cout << setw(PROPER_NUM) << setiosflags(ios::right) << setfill(' ') << copy_account
			<< setw(PROPER_NUM) << setiosflags(ios::right) << setfill(' ') << copy_name
			<< setw(PROPER_NUM / 2) << setiosflags(ios::right) << setfill(' ') << copy_rank
			<< setw(PROPER_NUM / 2) << setiosflags(ios::right) << setfill(' ') << copy_experience
			<< setw(PROPER_NUM / 2) << setiosflags(ios::right) << setfill(' ') << copy_num << endl;

	}
	AccountFile1.close();
	cout << "�������˺���Ϣ" << endl;

	cout << setw(PROPER_NUM) << setiosflags(ios::right) << setfill(' ') << "�˺�Ϊ��"
		<< setw(PROPER_NUM) << setiosflags(ios::right) << setfill(' ') << "�����Ϊ:"
		<< setw(PROPER_NUM / 2) << setiosflags(ios::right) << setfill(' ') << "�ȼ�Ϊ:"
		<< setw(PROPER_NUM / 2) << setiosflags(ios::right) << setfill(' ') << "����Ϊ:"
		<< setw(PROPER_NUM / 2) << setiosflags(ios::right) << setfill(' ') << "������:" << endl;

	ifstream AccountFile2(adm_inf);
	while (!AccountFile2.eof())
	{
		AccountFile2 >> copy_account
			>> copy_name
			>> copy_code
			>> copy_rank
			>> copy_experience
			>> copy_num;
		cout << setw(PROPER_NUM) << setiosflags(ios::right) << setfill(' ') << copy_account
			<< setw(PROPER_NUM) << setiosflags(ios::right) << setfill(' ') << copy_name
			<< setw(PROPER_NUM / 2) << setiosflags(ios::right) << setfill(' ') << copy_rank
			<< setw(PROPER_NUM / 2) << setiosflags(ios::right) << setfill(' ') << copy_experience
			<< setw(PROPER_NUM / 2) << setiosflags(ios::right) << setfill(' ') << copy_num << endl;
	}
	AccountFile2.close();
}

void individual::search_individual(int role, string player_inf, string  adm_inf)//�����Բ�ѯ�����Ϣ
{
	int in_command;
	char cmd_str[MAX_ARRAY_NUM];
	char cmd;
	system("cls");
	cout << "********************************************************" << endl;
	cout << "*                    ��ѡ���ѯ�ı�׼                  *" << endl;
	cout << "*    1���˺Ų�ѯ                2��������ѯ            *" << endl;
	cout << "*    3���ȼ���ѯ                4�������ѯ            *" << endl;
	cout << "*    5������(�ؿ�)��ѯ          6�˳�                  *" << endl;
	cout << "********************************************************" << endl;
	cin >> cmd_str;
	in_command = transfer_cmd(cmd_str);

	string cur_inf1 = "player_information.txt";
	string cur_inf2 = "adm_information.txt";

	char find_str[PROPER_NUM] = { '\0' };
	int find_int = 0;

	int back = 0;
	while (in_command != 6)
	{
		system("cls");
		switch (in_command)
		{
		case 1:
			cout << "�������ѯ�ߵ��˺�" << endl;
			cin >> find_str;
			cout << "�Դ����ߵĲ�ѯ��Ϣ����" << endl;
			back = account_search(find_str, cur_inf1);
			if (back == 0)
				cout << "�޸��˺Ŷ�Ӧ�Ĵ�����" << endl;
			cout << "�Գ����ߵĲ�ѯ��Ϣ����" << endl;
			back = account_search(find_str, cur_inf2);
			if (back == 0)
				cout << "�޸��˺Ŷ�Ӧ�ĳ�����" << endl;
			break;
		case 2:
			cout << "�������ѯ�ߵ�����" << endl;
			cin >> find_str;
			cout << "�Դ����ߵĲ�ѯ��Ϣ����" << endl;
			back = name_search(find_str, cur_inf1);
			if (back == 0)
				cout << "�޸��˺Ŷ�Ӧ�Ĵ�����" << endl;
			cout << "�Գ����ߵĲ�ѯ��Ϣ����" << endl;
			name_search(find_str, cur_inf2);
			if (back == 0)
				cout << "�޸��˺Ŷ�Ӧ�ĳ�����" << endl;
			break;
		case 3:
			cout << "�������ѯ�ߵĵȼ�" << endl;
			cin >> find_int;
			cout << "�Դ����ߵĲ�ѯ��Ϣ����" << endl;
			back = rank_search(find_int, cur_inf1);
			if (back == 0)
				cout << "�޸��˺Ŷ�Ӧ�Ĵ�����" << endl;
			cout << "�Գ����ߵĲ�ѯ��Ϣ����" << endl;
			back = rank_search(find_int, cur_inf2);
			if (back == 0)
				cout << "�޸��˺Ŷ�Ӧ�ĳ�����" << endl;
			break;
		case 4:
			cout << "�������ѯ�ߵľ���" << endl;
			cin >> find_int;
			cout << "�Դ����ߵĲ�ѯ��Ϣ����" << endl;
			back = exp_search(find_int, cur_inf1);
			if (back == 0)
				cout << "�޸��˺Ŷ�Ӧ�Ĵ�����" << endl;
			cout << "�Գ����ߵĲ�ѯ��Ϣ����" << endl;
			back = exp_search(find_int, cur_inf2);
			if (back == 0)
				cout << "�޸��˺Ŷ�Ӧ�ĳ�����" << endl;
			break;
		case 5:
			cout << "�������ѯ�ߵĳ���������������" << endl;
			cin >> find_int;
			cout << "�Դ����ߵĲ�ѯ��Ϣ����" << endl;
			back = num_search(find_int, cur_inf1);
			if (back == 0)
				cout << "�޸��˺Ŷ�Ӧ�Ĵ�����" << endl;
			cout << "�Գ����ߵĲ�ѯ��Ϣ����" << endl;
			back = num_search(find_int, cur_inf2);
			if (back == 0)
				cout << "�޸��˺Ŷ�Ӧ�ĳ�����" << endl;
			break;
		default: break;
		}
		cout << "********************************************************" << endl;
		cout << "*                    ��ѡ���ѯ�ı�׼                  *" << endl;
		cout << "*    1���˺Ų�ѯ                2��������ѯ            *" << endl;
		cout << "*    3���ȼ���ѯ                4�������ѯ            *" << endl;
		cout << "*    5������(�ؿ�)��ѯ          6�˳�                  *" << endl;
		cout << "********************************************************" << endl;
		cin >> cmd_str;
		in_command = transfer_cmd(cmd_str);
	}
	system("cls");
}

int individual::account_search(char find_str[], string cur_inf)//�����˺Ų�ѯ
{
	char copy_account[PROPER_NUM] = { '\0' },
		copy_name[PROPER_NUM] = { '\0' },
		copy_code[PROPER_NUM] = { '\0' };
	int copy_rank, copy_experience, copy_num;

	int i = 0;
	ifstream AccountFile1(cur_inf);
	while (!AccountFile1.eof())
	{
		AccountFile1 >> copy_account
			>> copy_name
			>> copy_code
			>> copy_rank
			>> copy_experience
			>> copy_num;
		if (strcmp(find_str, copy_account) == 0)
		{
			if (i == 0)
			{
				cout << setw(PROPER_NUM) << setiosflags(ios::right) << setfill(' ') << "�˺�Ϊ��"
					<< setw(PROPER_NUM) << setiosflags(ios::right) << setfill(' ') << "�����Ϊ:"
					<< setw(PROPER_NUM / 2) << setiosflags(ios::right) << setfill(' ') << "�ȼ�Ϊ:"
					<< setw(PROPER_NUM / 2) << setiosflags(ios::right) << setfill(' ') << "����Ϊ:"
					<< setw(PROPER_NUM / 2) << setiosflags(ios::right) << setfill(' ') << "����/������:" << endl;
			}
			i++;
			cout << setw(PROPER_NUM) << setiosflags(ios::right) << setfill(' ') << copy_account
				<< setw(PROPER_NUM) << setiosflags(ios::right) << setfill(' ') << copy_name
				<< setw(PROPER_NUM / 2) << setiosflags(ios::right) << setfill(' ') << copy_rank
				<< setw(PROPER_NUM / 2) << setiosflags(ios::right) << setfill(' ') << copy_experience
				<< setw(PROPER_NUM / 2) << setiosflags(ios::right) << setfill(' ') << copy_num << endl;
		}

	}
	return i;
}

int individual::name_search(char find_str[], string cur_inf)//��������������в�ѯ
{
	char copy_account[PROPER_NUM] = { '\0' },
		copy_name[PROPER_NUM] = { '\0' },
		copy_code[PROPER_NUM] = { '\0' };
	int copy_rank, copy_experience, copy_num;

	int i = 0;
	ifstream AccountFile1(cur_inf);
	while (!AccountFile1.eof())
	{
		AccountFile1 >> copy_account
			>> copy_name
			>> copy_code
			>> copy_rank
			>> copy_experience
			>> copy_num;
		if (strcmp(find_str, copy_name) == 0)
		{
			if (i == 0)
			{
				cout << setw(PROPER_NUM) << setiosflags(ios::right) << setfill(' ') << "�˺�Ϊ��"
					<< setw(PROPER_NUM) << setiosflags(ios::right) << setfill(' ') << "�����Ϊ:"
					<< setw(PROPER_NUM / 2) << setiosflags(ios::right) << setfill(' ') << "�ȼ�Ϊ:"
					<< setw(PROPER_NUM / 2) << setiosflags(ios::right) << setfill(' ') << "����Ϊ:"
					<< setw(PROPER_NUM / 2) << setiosflags(ios::right) << setfill(' ') << "����/������:" << endl;
			}
			i++;
			cout << setw(PROPER_NUM) << setiosflags(ios::right) << setfill(' ') << copy_account
				<< setw(PROPER_NUM) << setiosflags(ios::right) << setfill(' ') << copy_name
				<< setw(PROPER_NUM / 2) << setiosflags(ios::right) << setfill(' ') << copy_rank
				<< setw(PROPER_NUM / 2) << setiosflags(ios::right) << setfill(' ') << copy_experience
				<< setw(PROPER_NUM / 2) << setiosflags(ios::right) << setfill(' ') << copy_num << endl;
		}

	}
	return i;
}

int individual::rank_search(int find_int, string cur_inf)//���յȼ����в�ѯ
{
	string copy_account, copy_name, copy_code;
	int copy_rank, copy_experience, copy_num;

	int i = 0;
	ifstream AccountFile1(cur_inf);
	while (!AccountFile1.eof())
	{
		AccountFile1 >> copy_account
			>> copy_name
			>> copy_code
			>> copy_rank
			>> copy_experience
			>> copy_num;
		if (find_int == copy_rank)
		{
			if (i == 0)
			{
				cout << setw(PROPER_NUM) << setiosflags(ios::right) << setfill(' ') << "�˺�Ϊ��"
					<< setw(PROPER_NUM) << setiosflags(ios::right) << setfill(' ') << "�����Ϊ:"
					<< setw(PROPER_NUM / 2) << setiosflags(ios::right) << setfill(' ') << "�ȼ�Ϊ:"
					<< setw(PROPER_NUM / 2) << setiosflags(ios::right) << setfill(' ') << "����Ϊ:"
					<< setw(PROPER_NUM / 2) << setiosflags(ios::right) << setfill(' ') << "����/������:" << endl;
			}
			i++;
			cout << setw(PROPER_NUM) << setiosflags(ios::left) << setfill(' ') << copy_account
				<< setw(PROPER_NUM) << setiosflags(ios::left) << setfill(' ') << copy_name
				<< setw(PROPER_NUM / 2) << setiosflags(ios::right) << setfill(' ') << copy_rank
				<< setw(PROPER_NUM / 2) << setiosflags(ios::right) << setfill(' ') << copy_experience
				<< setw(PROPER_NUM / 2) << setiosflags(ios::right) << setfill(' ') << copy_num << endl;
		}

	}
	return i;
}

int individual::exp_search(int find_int, string cur_inf)//���վ�����в�ѯ
{
	string copy_account, copy_name, copy_code;
	int copy_rank, copy_experience, copy_num;

	int i = 0;
	ifstream AccountFile1(cur_inf);
	while (!AccountFile1.eof())
	{
		AccountFile1 >> copy_account
			>> copy_name
			>> copy_code
			>> copy_rank
			>> copy_experience
			>> copy_num;
		if (find_int == copy_experience)
		{
			if (i == 0)
			{
				cout << setw(PROPER_NUM) << setiosflags(ios::right) << setfill(' ') << "�˺�Ϊ��"
					<< setw(PROPER_NUM) << setiosflags(ios::right) << setfill(' ') << "�����Ϊ:"
					<< setw(PROPER_NUM / 2) << setiosflags(ios::right) << setfill(' ') << "�ȼ�Ϊ:"
					<< setw(PROPER_NUM / 2) << setiosflags(ios::right) << setfill(' ') << "����Ϊ:"
					<< setw(PROPER_NUM / 2) << setiosflags(ios::right) << setfill(' ') << "����/������:" << endl;
			}
			i++;
			cout << setw(PROPER_NUM) << setiosflags(ios::right) << setfill(' ') << copy_account
				<< setw(PROPER_NUM) << setiosflags(ios::right) << setfill(' ') << copy_name
				<< setw(PROPER_NUM / 2) << setiosflags(ios::right) << setfill(' ') << copy_rank
				<< setw(PROPER_NUM / 2) << setiosflags(ios::right) << setfill(' ') << copy_experience
				<< setw(PROPER_NUM / 2) << setiosflags(ios::right) << setfill(' ') << copy_num << endl;
		}

	}
	return i;
}

int individual::num_search(int find_int, string cur_inf)//���ճ��������ߴ��������в�ѯ
{
	string copy_account, copy_name, copy_code;
	int copy_rank, copy_experience, copy_num;

	int i = 0;
	ifstream AccountFile1(cur_inf);
	while (!AccountFile1.eof())
	{
		AccountFile1 >> copy_account
			>> copy_name
			>> copy_code
			>> copy_rank
			>> copy_experience
			>> copy_num;
		if (find_int == copy_num)
		{
			if (i == 0)
			{
				cout << setw(PROPER_NUM) << setiosflags(ios::right) << setfill(' ') << "�˺�Ϊ��"
					<< setw(PROPER_NUM) << setiosflags(ios::right) << setfill(' ') << "�����Ϊ:"
					<< setw(PROPER_NUM / 2) << setiosflags(ios::right) << setfill(' ') << "�ȼ�Ϊ:"
					<< setw(PROPER_NUM / 2) << setiosflags(ios::right) << setfill(' ') << "����Ϊ:"
					<< setw(PROPER_NUM / 2) << setiosflags(ios::right) << setfill(' ') << "����/������:" << endl;
			}
			i++;
			cout << setw(PROPER_NUM) << setiosflags(ios::right) << setfill(' ') << copy_account
				<< setw(PROPER_NUM) << setiosflags(ios::right) << setfill(' ') << copy_name
				<< setw(PROPER_NUM / 2) << setiosflags(ios::right) << setfill(' ') << copy_rank
				<< setw(PROPER_NUM / 2) << setiosflags(ios::right) << setfill(' ') << copy_experience
				<< setw(PROPER_NUM / 2) << setiosflags(ios::right) << setfill(' ') << copy_num << endl;
		}

	}
	return i;
}

int transfer_cmd(char *command)//��������ת������
{
	int i=0;
	switch (command[0])
	{
	case '1':
		i = 1;
		break;
	case '2':
		i = 2;
		break;
	case '3':
		i = 3;
		break;
	case '4':
		i = 4;
		break;
	case '5':
		i = 5;
		break;
	case '6':
		i = 6;
		break;
	case '7':
		i = 7;
		break;
	case '8':
		i = 8;
		break;
	case '9':
		i = 9;
		break;
	default:
		i = 0;
		break;
	}
	return i;
}
