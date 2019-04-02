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

individual::individual()
	:user_experience(0), sort_standard(0), user_rank(0), que_or_passnum(0), client(0), v_client1(0), v_client2(0)
{
	ZeroMemory(user_name, PROPER_NUM);
	ZeroMemory(game_account, PROPER_NUM);
	ZeroMemory(user_password, PROPER_NUM);
}

individual::individual(char *account, char *name, char *password,
	int experience, int standard, int rank, int num, int _client, int _v_client1,int _v_client2)
	:user_experience(experience), sort_standard(standard),
	user_rank(rank), que_or_passnum(que_or_passnum), client(_client)
	, v_client1(_v_client1), v_client2(_v_client2)
{
	strcpy(game_account, account);
	strcpy(user_name, name);
	strcpy(user_password, password);
}

individual::individual(const individual& I)
	       :user_experience(I.user_experience), sort_standard(I.sort_standard),
			user_rank(I.user_rank), que_or_passnum(I.que_or_passnum), 
			client(I.client), v_client1(I.v_client1), v_client2(I.v_client2)
{
	strcpy(game_account, I.game_account);
	strcpy(user_name, I.user_name);
	strcpy(user_password, I.user_password);

}

void individual::change_username()             //���Խ���ע�����������޸�
{
	int command;
	char recvebuf[BUF_SIZE], sendbuf[BUF_SIZE] = { "\0" };
	ZeroMemory(sendbuf, BUF_SIZE);       //������������޸���������
	command = CHANGE_NAME;
	memcpy(sendbuf, &command, 4);
	int retVal = send(client, sendbuf, strlen(sendbuf), 0);
	// ���շ������˵�ȷ�ϣ�
	ZeroMemory(recvebuf, BUF_SIZE);
	recv(client, recvebuf, BUF_SIZE, 0);	

	if (recvebuf[0] == 'Y')
	{
		cout << "�������µ��û���";
		ZeroMemory(sendbuf, BUF_SIZE);
		cin >> sendbuf;
		send(client, sendbuf, strlen(sendbuf), 0);

		ZeroMemory(recvebuf, BUF_SIZE);
		recv(client, recvebuf, BUF_SIZE, 0);		// ���շ������˵����ݣ�

		if (recvebuf[0] == 'Y')
		{
			ZeroMemory(user_name, PROPER_NUM);
			strcpy(user_name,sendbuf);
			cout << "�����޸ĳɹ�" << endl;
		}
		else
		{
			cout << "�����޸�ʧ�ܣ����Ժ�����" << endl;
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

void individual::change_password()  //�޸�����
{
	int command;
	char recvebuf[BUF_SIZE], sendbuf[BUF_SIZE] = { "\0" };

	ZeroMemory(sendbuf, BUF_SIZE);       //�������������
	command = CHANGE_PASSWORD;
	memcpy(sendbuf, &command, 4);
	int retVal = send(client, sendbuf, strlen(sendbuf), 0);

	// ���շ������˵�ȷ�ϣ�
	ZeroMemory(recvebuf, BUF_SIZE);
	recv(client, recvebuf, BUF_SIZE, 0);
	if (recvebuf[0] == 'Y')
	{
		string old_password, new_password;
		cout << "������ɵ�����";
		cin >> old_password;
		cout << "�������µ�����";
		cin >> new_password;
		cout << "���ٴ������µ�����";
		ZeroMemory(sendbuf, BUF_SIZE);
		cin >> sendbuf;
		if (new_password == sendbuf&&old_password == user_password)
		{
			send(client, sendbuf, strlen(sendbuf), 0);

			ZeroMemory(recvebuf, BUF_SIZE);
			recv(client, recvebuf, BUF_SIZE, 0);		// ���շ������˵����ݣ�

			if (recvebuf[0] == 'Y')
			{
				ZeroMemory(user_password, PROPER_NUM);
				strcpy(user_password, sendbuf);
				cout << "�����޸ĳɹ�" << endl;
			}
			else
			{
				cout << "�����޸�ʧ�ܣ����Ժ�����" << endl;
			}
		}
		else if (new_password == sendbuf)
		{
			cout << "�������������"<<endl;
		}
		else
			cout << "�������������벻һ��"<<endl;
		ZeroMemory(sendbuf, BUF_SIZE);
		sendbuf[0] = '*';
		send(client, sendbuf, strlen(sendbuf), 0);
	}
	else
	{
		cout << "��������æ�����Ժ�����" << endl;
		ZeroMemory(sendbuf, BUF_SIZE);
		sendbuf[0] = '*';
		send(client, sendbuf, strlen(sendbuf), 0);
	}
}

int individual::user_register(int role)      //���ע��
{
	system("cls");
	int command;
	char recvebuf[BUF_SIZE], sendbuf[BUF_SIZE] = { "\0" };
	ZeroMemory(sendbuf, BUF_SIZE);       //���������������
	command = REGISTER;
	memcpy(sendbuf, &command, 4);
	int retVal = send(client, sendbuf, strlen(sendbuf), 0);
	
	ZeroMemory(recvebuf, BUF_SIZE);
	recv(client, recvebuf, BUF_SIZE, 0);		// ���շ������˵����ݣ�
	if (recvebuf[0] == 'Y')
	{
	    ZeroMemory(sendbuf, BUF_SIZE);
		memcpy(sendbuf,&role,4);
		send(client, sendbuf, strlen(sendbuf), 0);
		ZeroMemory(recvebuf, BUF_SIZE);
	    recv(client, recvebuf, BUF_SIZE, 0);
		cout << "������ע����Ϸ�˺�";
		ZeroMemory(sendbuf, BUF_SIZE);
		cin >> sendbuf;
		send(client, sendbuf, strlen(sendbuf), 0);

		ZeroMemory(recvebuf, BUF_SIZE);
		recv(client, recvebuf, BUF_SIZE, 0);		// ���շ������˵����ݣ�

		if (recvebuf[0] == 'Y')
		{
		cout << "����������";
		ZeroMemory(sendbuf, BUF_SIZE);
		cin >> sendbuf;
		send(client, sendbuf, strlen(sendbuf), 0);

		ZeroMemory(recvebuf, BUF_SIZE);
		recv(client, recvebuf, BUF_SIZE, 0);
			
			cout << "����������";
			string code;
			cin >> code;
			cout << "���ٴ���������";
			cin >> sendbuf;
			while (code != sendbuf)
			{
				cout << "����ǰ��һ�£�����������" << endl;
				cout << "����������";
				cin >> code;
				ZeroMemory(sendbuf, BUF_SIZE);
				cout << "���ٴ���������";
				cin >> sendbuf;
			}
			send(client, sendbuf, strlen(sendbuf), 0);
			ZeroMemory(recvebuf, BUF_SIZE);
			recv(client, recvebuf, BUF_SIZE, 0);

			if (recvebuf[0] == 'Y')
			{
				cout << "ע��ɹ���" << endl;
				return TRUE;
			}
			else
			{
				cout << "ע��ʧ��";
				return FALSE;
			}
		}
		else
		{
			cout << "���˺��Ѿ�����" << endl;
			return FALSE;
		}
	}
	else
	{
		cout << "��������æ" << endl;
		ZeroMemory(sendbuf, BUF_SIZE);
		sendbuf[0] = '*';
		send(client, sendbuf, strlen(sendbuf), 0);
		return FALSE;
	}	
}

int individual::user_login(int role)       //��ҵ�½
{
	system("cls");
	int command;
	char recvebuf[BUF_SIZE], sendbuf[BUF_SIZE] = { "\0" };

	ZeroMemory(sendbuf, BUF_SIZE);       //���������������
	command = LOGIN;
	memcpy(sendbuf, &command, 4);
	int retVal = send(client, sendbuf, strlen(sendbuf), 0);
	ZeroMemory(recvebuf, BUF_SIZE);
	recv(client, recvebuf, BUF_SIZE, 0);		// ���շ������˵����ݣ�
	if (recvebuf[0] == 'Y')
	{
		ZeroMemory(sendbuf, BUF_SIZE);
		memcpy(sendbuf,&role,4);
		send(client, sendbuf, strlen(sendbuf), 0);
		ZeroMemory(recvebuf, BUF_SIZE);
	    recv(client, recvebuf, BUF_SIZE, 0);
		//system("pause");

		cout << "��������Ϸ�˺�";
		ZeroMemory(sendbuf, BUF_SIZE);
		cin >> sendbuf;
		send(client, sendbuf, strlen(sendbuf), 0);

		ZeroMemory(recvebuf, BUF_SIZE);
		recv(client, recvebuf, BUF_SIZE, 0);		// ���շ������˵����ݣ�

		if (recvebuf[0] == 'Y')
		{
			ZeroMemory(game_account, PROPER_NUM);
			strcpy(game_account, sendbuf);
			//���˺�ͬ��������
			cout << "����������";
			ZeroMemory(sendbuf, BUF_SIZE);
			cin >> sendbuf;
			send(client, sendbuf, strlen(sendbuf), 0);
			ZeroMemory(recvebuf, BUF_SIZE);
			recv(client, recvebuf, BUF_SIZE, 0);

			if (recvebuf[0] == 'Y')
			{
				ZeroMemory(user_password, PROPER_NUM);
				strcpy(user_password, sendbuf);
				//������ͬ��������
				ZeroMemory(sendbuf, BUF_SIZE);
				sendbuf[0] = 'Y';
				send(client, sendbuf, strlen(sendbuf), 0);
				ZeroMemory(recvebuf, BUF_SIZE);
				recv(client, recvebuf, BUF_SIZE, 0);
				ZeroMemory(user_name, PROPER_NUM);
				strcpy(user_name, recvebuf);
				//��������������]

				memcpy(user_name, recvebuf, PROPER_NUM);
				send(client, sendbuf, strlen(sendbuf), 0);
				//cout << "labuabulabu";
				ZeroMemory(recvebuf, BUF_SIZE);
				recv(client, recvebuf, BUF_SIZE, 0);
				memcpy(&user_rank, recvebuf, 4);   //���ܵȼ�������
				user_rank--;

				send(client, sendbuf, strlen(sendbuf), 0);
				ZeroMemory(recvebuf, BUF_SIZE);
				recv(client, recvebuf, BUF_SIZE, 0);
				memcpy(&user_experience, recvebuf, 4);   //���ܾ���
				user_experience--;

				send(client, sendbuf, strlen(sendbuf), 0);
				ZeroMemory(recvebuf, BUF_SIZE);
				recv(client, recvebuf, BUF_SIZE, 0);
				memcpy(&que_or_passnum, recvebuf, 4);    //���ܳ��������ߴ�����
				que_or_passnum--;
				//system("pause");

				ZeroMemory(sendbuf, BUF_SIZE);
				sendbuf[0] = 'Y';
				send(client, sendbuf, strlen(sendbuf), 0);
				ZeroMemory(recvebuf, BUF_SIZE);
				recv(client, recvebuf, BUF_SIZE, 0);
				if (recvebuf[0] == 'Y')
				{
					cout << "��½�ɹ���" << endl;
					return TRUE;
				}
				else
				{
					cout << "���˺��Ѿ��ڱ𴦵�½�����Ժ�����" << endl;
					return FALSE;
				}
			}
			else
			{
				cout << "��½ʧ�ܣ���������״���Լ��˺��������Ϣ"<<endl;
				return FALSE;
			}
		}
		else
		{
			cout << "���˺Ų�����" << endl;
			return FALSE;
		}
	}
	else
	{
		cout << "��������æ" << endl;
		ZeroMemory(sendbuf, BUF_SIZE);
		sendbuf[0] = '*';
		send(client, sendbuf, strlen(sendbuf), 0);
		return FALSE;
	}
}



