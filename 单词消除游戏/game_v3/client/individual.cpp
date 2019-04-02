#include <Winsock2.h>
#include<iostream>
#include<fstream>
#include<string>
#include<iomanip>
#include<windows.h>
#include"mylib.h"
#include"individual.h"
#pragma comment(lib,"ws2_32.lib")
using namespace std;

void individual::change(int role, int pass_num, int cur_experience)
{
	int command;
	char recvebuf[BUF_SIZE], sendbuf[BUF_SIZE] = { "\0" };

	ZeroMemory(sendbuf, BUF_SIZE);       //���������������
	command = CHANGE;
	memcpy(sendbuf, &command, 4);
	int retVal = send(client, sendbuf, strlen(sendbuf), 0);

	ZeroMemory(recvebuf, BUF_SIZE);
	recv(client, recvebuf, BUF_SIZE, 0);
	if (recvebuf[0] == 'Y')
	{
		que_or_passnum = pass_num;
		if ((cur_experience + user_experience) >= 0)//��֤�ȼ����������鲻��Ϊ������ ��Ϊ��ս����׼��
		{
			user_experience = user_experience + cur_experience;
		}
		else
			user_experience = 0;

		if (user_experience >= ((user_rank + 1)*INC_RANK_RATIO))//����������Ҫ��󣬻��������
		{
			user_experience = user_experience - ((user_rank + 1)*INC_RANK_RATIO);
			user_rank++;
		}
		ZeroMemory(sendbuf, BUF_SIZE);
		memcpy(sendbuf, &role, 4);
		send(client, sendbuf, strlen(sendbuf), 0);
	
		recv(client, recvebuf, BUF_SIZE, 0);
		ZeroMemory(sendbuf, BUF_SIZE);
		pass_num++;
		memcpy(sendbuf, &pass_num, 4);
		send(client, sendbuf, strlen(sendbuf), 0);
		recv(client, recvebuf, BUF_SIZE, 0);

		ZeroMemory(sendbuf, BUF_SIZE);
		cur_experience++;
		memcpy(sendbuf, &cur_experience, 4);
		send(client, sendbuf, strlen(sendbuf), 0);
		ZeroMemory(recvebuf, BUF_SIZE);
		recv(client, recvebuf, BUF_SIZE, 0);          //ͬʱ�������Ϣ���͸����������ڷ������˿ڶ���Ҿ������Ϣ�����޸�

		if (recvebuf[0] != 'Y')
		{
			cout << "���������ӳ�������" << endl;
		}
	}
	else
	{
		cout << "��������æ�����Ժ�����" << endl;
		ZeroMemory(sendbuf, BUF_SIZE);
		sendbuf[0] = '*';
		send(client, sendbuf, strlen(sendbuf), 0);
	}
}

void individual::search_All_individual()       //���������ǰ����Ϸ��ע������е����
{
	int command;
	char recvebuf[BUF_SIZE], sendbuf[BUF_SIZE] = { "\0" };

	ZeroMemory(sendbuf, BUF_SIZE);       //���������������
	command = SEARCH_ALL;
	memcpy(sendbuf, &command, 4);
	send(client, sendbuf, strlen(sendbuf), 0);

	ZeroMemory(recvebuf, BUF_SIZE);
	recv(client, recvebuf, BUF_SIZE, 0);
	if (recvebuf[0] == 'Y')
	{
		cout << "��������Ϣ"<<endl;      //��������ߵ�������Ϣ

		cout<< setw(PROPER_NUM) << setiosflags(ios::left) << setfill(' ') << "�˺�Ϊ��"
			<< setw(PROPER_NUM) << setiosflags(ios::left) << setfill(' ') << "�����Ϊ:"
			<< setw(PROPER_NUM/2) << setiosflags(ios::right) << setfill(' ') << "�ȼ�Ϊ:"
			<< setw(PROPER_NUM/2) << setiosflags(ios::right) << setfill(' ') << "����Ϊ:"
			<< setw(PROPER_NUM/2) << setiosflags(ios::right) << setfill(' ') << "������:" << endl;
		int i = 0;
		ZeroMemory(sendbuf, BUF_SIZE);
		sendbuf[0] = 'Y';
		send(client, sendbuf, strlen(sendbuf), 0);
		ZeroMemory(recvebuf, BUF_SIZE);
		recv(client, recvebuf, BUF_SIZE, 0);

		while (recvebuf[0] != 'N')
		{
			
			if ((i % 5) < 2)
			{
				cout << setw(PROPER_NUM) << setiosflags(ios::left) << setfill(' ') << recvebuf;
			}
			else 
			{
				int j = 0;
				memcpy(&j, recvebuf, 4);
				cout << setw(PROPER_NUM/2) << setiosflags(ios::right) << setfill(' ') << j-1;
			}
			i++;
			if ((i % 5) == 0)
				cout << endl;

			ZeroMemory(sendbuf, BUF_SIZE);
			sendbuf[0] = 'Y';
			send(client, sendbuf, strlen(sendbuf), 0);
			ZeroMemory(recvebuf, BUF_SIZE);
			recv(client, recvebuf, BUF_SIZE, 0);
		}

		ZeroMemory(sendbuf, BUF_SIZE);
		sendbuf[0] = 'Y';
		send(client, sendbuf, strlen(sendbuf), 0);
		cout << "��������Ϣ" << endl;       //��������ߵ����е���Ϣ
		ZeroMemory(recvebuf, BUF_SIZE);
		recv(client, recvebuf, BUF_SIZE, 0);
		cout << setw(PROPER_NUM) << setiosflags(ios::left) << setfill(' ') << "�˺�Ϊ��"
			 << setw(PROPER_NUM) << setiosflags(ios::left) << setfill(' ') << "�����Ϊ:"
			 << setw(PROPER_NUM/2) << setiosflags(ios::right) << setfill(' ') << "�ȼ�Ϊ:"
			 << setw(PROPER_NUM/2) << setiosflags(ios::right) << setfill(' ') << "����Ϊ:"
			 << setw(PROPER_NUM/2) << setiosflags(ios::right) << setfill(' ') << "������:" << endl;

		i = 0;
		ZeroMemory(sendbuf, BUF_SIZE);
		sendbuf[0] = 'Y';
		send(client, sendbuf, strlen(sendbuf), 0);
		ZeroMemory(recvebuf, BUF_SIZE);
		recv(client, recvebuf, BUF_SIZE, 0);

		while (recvebuf[0] != 'N')
		{

			if ((i % 5) < 2)
			{
				cout << setw(PROPER_NUM) << setiosflags(ios::left) << setfill(' ') << recvebuf;
			}
			else
			{
				int j = 0;
				memcpy(&j, recvebuf, 4);
				cout << setw(PROPER_NUM / 2) << setiosflags(ios::right) << setfill(' ') << j - 1;
			}
			i++;
			if ((i % 5) == 0)
				cout << endl;

			ZeroMemory(sendbuf, BUF_SIZE);
			sendbuf[0] = 'Y';
			send(client, sendbuf, strlen(sendbuf), 0);
			ZeroMemory(recvebuf, BUF_SIZE);
			recv(client, recvebuf, BUF_SIZE, 0);
		}
	}
	else
	{
		cout << "��������æ�����Ժ�����" << endl;
		ZeroMemory(sendbuf, BUF_SIZE);
		sendbuf[0] = '*';
		send(client, sendbuf, strlen(sendbuf), 0);
	}
}

void individual::search_individual()   //�������Խ��в�ѯ
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
	cmd = cmd_str[0];
	in_command = transfer_cmd(cmd);

	char information[PROPER_NUM] = { '\0' };
	while (in_command != 6)
	{
		system("cls");
		switch (in_command)
		{
		case 1:
			search(1);
			break;
		case 2:
			search(2);
			break;
		case 3:
			search(3 );
			break;
		case 4:
			search(4);
			break;
		case 5:
			search(5);
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
		cmd = cmd_str[0];
		in_command = transfer_cmd(cmd);
	}
	system("cls");
}

void individual::search(int num)     //�����Բ�ѯʱ���ĳ����������������Ϣ���������
{
	int command;
	char recvebuf[BUF_SIZE], sendbuf[BUF_SIZE] = { "\0" };
	int in_find_inf;

	ZeroMemory(sendbuf, BUF_SIZE);
	command = SEARCH_ONES;
	memcpy(sendbuf, &command, 4);
	send(client, sendbuf, strlen(sendbuf), 0);//��ѯ�����ȥ
	ZeroMemory(recvebuf, BUF_SIZE);
	recv(client, recvebuf, BUF_SIZE, 0);

	ZeroMemory(sendbuf, BUF_SIZE);
	memcpy(sendbuf, &num, 4);
	send(client, sendbuf, strlen(sendbuf), 0);//���ڲ�С�����ȥ
	ZeroMemory(recvebuf, BUF_SIZE);
	recv(client, recvebuf, BUF_SIZE, 0);

	if (recvebuf[0] == 'Y')
	{
		switch (num)
		{
		case 1:

			cout << "�������ѯ�ߵ��˺�" << endl;
			ZeroMemory(sendbuf, BUF_SIZE);
			cin >> sendbuf;
			send(client, sendbuf, strlen(sendbuf), 0);
			ZeroMemory(recvebuf, BUF_SIZE);
			recv(client, recvebuf, BUF_SIZE, 0);

			break;
		case 2:
			cout << "�������ѯ�ߵ�����" << endl;
			ZeroMemory(sendbuf, BUF_SIZE);
			cin >> sendbuf;
			send(client, sendbuf, strlen(sendbuf), 0);
			ZeroMemory(recvebuf, BUF_SIZE);
			recv(client, recvebuf, BUF_SIZE, 0);

			break;
		case 3:
			cout << "�������ѯ�ߵĵȼ�" << endl;
			ZeroMemory(sendbuf, BUF_SIZE);
			cin >> in_find_inf;
			in_find_inf++;
			memcpy(sendbuf, &in_find_inf, 4);
			send(client, sendbuf, strlen(sendbuf), 0);
			ZeroMemory(recvebuf, BUF_SIZE);
			recv(client, recvebuf, BUF_SIZE, 0);

			break;
		case 4:
			cout << "�������ѯ�ߵľ���" << endl;
			ZeroMemory(sendbuf, BUF_SIZE);
			cin >> in_find_inf;
			in_find_inf++;
			memcpy(sendbuf,&in_find_inf,4);
			send(client, sendbuf, strlen(sendbuf), 0);
			ZeroMemory(recvebuf, BUF_SIZE);
			recv(client, recvebuf, BUF_SIZE, 0);

			break;
		case 5:
			cout << "�������ѯ�˺ŵĹؿ�����������" << endl;
			ZeroMemory(sendbuf, BUF_SIZE);
			cin >> in_find_inf;
			in_find_inf++;
			memcpy(sendbuf, &in_find_inf, 4);
			send(client, sendbuf, strlen(sendbuf), 0);
			ZeroMemory(recvebuf, BUF_SIZE);
			recv(client, recvebuf, BUF_SIZE, 0);

			break;
		default: break;
		}
		cout << "�Դ����ߵĲ�ѯ��Ϣ����" << endl;

		if ((recvebuf[0] == '-') && (recvebuf[1] == '>'))
		{
			cout << "�޸���Ϣ��Ӧ�Ĵ�����" << endl;
		}
		else
		{
			cout << setw(PROPER_NUM) << setiosflags(ios::left) << setfill(' ') << "�˺�Ϊ��"
				<< setw(PROPER_NUM) << setiosflags(ios::left) << setfill(' ') << "�����Ϊ:"
				<< setw(PROPER_NUM / 2) << setiosflags(ios::right) << setfill(' ') << "�ȼ�Ϊ:"
				<< setw(PROPER_NUM / 2) << setiosflags(ios::right) << setfill(' ') << "����Ϊ:"
				<< setw(PROPER_NUM / 2) << setiosflags(ios::right) << setfill(' ') << "������:" << endl;
			int i = 0;
			while ((recvebuf[0] != '-') || (recvebuf[1] != '>'))
			{
				if ((i % 5) < 2)
				{
					cout << setw(PROPER_NUM) << setiosflags(ios::left) << setfill(' ') << recvebuf;
				}
				else
				{
					int j = 0;
					memcpy(&j, recvebuf, 4);
					cout << setw(PROPER_NUM / 2) << setiosflags(ios::right) << setfill(' ') << j - 1;
				}
				i++;
				if ((i % 5) == 0)
					cout << endl;

				ZeroMemory(sendbuf, BUF_SIZE);
				sendbuf[0] = 'Y';
				send(client, sendbuf, strlen(sendbuf), 0);
				ZeroMemory(recvebuf, BUF_SIZE);
				recv(client, recvebuf, BUF_SIZE, 0);
			}
		}

		ZeroMemory(sendbuf, BUF_SIZE);
		sendbuf[0] = 'Y';
		send(client, sendbuf, strlen(sendbuf), 0);
		ZeroMemory(recvebuf, BUF_SIZE);
		recv(client, recvebuf, BUF_SIZE, 0);

		cout << "�Գ����ߵĲ�ѯ��Ϣ����" << endl;
		if ((recvebuf[0] == '-') && (recvebuf[1] == '>'))
		{
			cout << "�޸���Ϣ��Ӧ�ĳ�����" << endl;
		}
		else
		{
			cout << setw(PROPER_NUM) << setiosflags(ios::left) << setfill(' ') << "�˺�Ϊ��"
				<< setw(PROPER_NUM) << setiosflags(ios::left) << setfill(' ') << "�����Ϊ:"
				<< setw(PROPER_NUM / 2) << setiosflags(ios::right) << setfill(' ') << "�ȼ�Ϊ:"
				<< setw(PROPER_NUM / 2) << setiosflags(ios::right) << setfill(' ') << "����Ϊ:"
				<< setw(PROPER_NUM / 2) << setiosflags(ios::right) << setfill(' ') << "������:" << endl;
			int i=0 ;
			while ((recvebuf[0] != '-') || (recvebuf[1] != '>'))
			{
				if ((i % 5) < 2)
				{
					cout << setw(PROPER_NUM) << setiosflags(ios::left) << setfill(' ') << recvebuf;
				}
				else
				{
					int j = 0;
					memcpy(&j, recvebuf, 4);
					cout << setw(PROPER_NUM / 2) << setiosflags(ios::right) << setfill(' ') << j - 1;
				}
				i++;
				if ((i % 5) == 0)
					cout << endl;

				ZeroMemory(sendbuf, BUF_SIZE);
				sendbuf[0] = 'Y';
				send(client, sendbuf, strlen(sendbuf), 0);
				ZeroMemory(recvebuf, BUF_SIZE);
				recv(client, recvebuf, BUF_SIZE, 0);
			}
		}
	}
	else
	{
		cout << "��������æ�����Ժ�����" << endl;
		ZeroMemory(sendbuf, BUF_SIZE);
		sendbuf[0] = '*';
		send(client, sendbuf, strlen(sendbuf), 0);
	}
}

int transfer_cmd(char command)          //�������������װ�����Ժ�����������ݴ���
{
	int i=0;
	switch (command)
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