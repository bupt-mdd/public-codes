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

void gamer::listen()
{
	char recvebuf[BUF_SIZE], sendbuf[BUF_SIZE] = { "\0" };
	char copy_account[MAX_ARRAY_NUM] = { '\0' };
	char account[MAX_ARRAY_NUM] = { '\0' };
	char copy_name[MAX_ARRAY_NUM] = { '\0' };
	char name[MAX_ARRAY_NUM] = { '\0' };

	while (true)
	{
		Sleep(1);
		while (listen_lab == SET_QUE_MAN)
			Sleep(1000);
		ZeroMemory(recvebuf, BUF_SIZE);
		recv(v_client1, recvebuf, BUF_SIZE, 0);
		int command;
		memcpy(&command, recvebuf, 4);
		if(command==REC_CHALLANGE)
		{
			if (challange_lab==FALSE)
			{
				if (whether != FALSE)
				{
					ZeroMemory(sendbuf, BUF_SIZE);
					sendbuf[0] = 'N';
					send(v_client1, sendbuf, strlen(sendbuf), 0);//����ȷ��
				}
				else
				{
					ZeroMemory(sendbuf, BUF_SIZE);
					sendbuf[0] = 'Y';
					send(v_client1, sendbuf, strlen(sendbuf), 0);//����ȷ��
					ZeroMemory(recvebuf, BUF_SIZE);
					recv(v_client1, recvebuf, BUF_SIZE, 0);//������ս�ߵ��˺���
					strcpy(challange_account, recvebuf);

					ZeroMemory(sendbuf, BUF_SIZE);
					sendbuf[0] = 'Y';
					send(v_client1, sendbuf, strlen(sendbuf), 0);//����ȷ��
					ZeroMemory(recvebuf, BUF_SIZE);
					recv(v_client1, recvebuf, BUF_SIZE, 0);//������ս�ߵ�����
					strcpy(challange_name, recvebuf);

					whether = TRUE;
					cout << endl << "��Ϣ����ʾ" << challange_account << "���㷢������ս" << endl;
				}
			}
			else
			{
				ZeroMemory(sendbuf, BUF_SIZE);
				sendbuf[0] = 'N';
				sendbuf[1] = 'N';
				send(v_client1, sendbuf, strlen(sendbuf), 0);//����ȷ��
			}
		} 
		else
		{
			if (close != FALSE)
				return;             //ͨ��return�������߳�
			whether = FALSE;
			cout << endl << "��Ϣ����ʾ��" << challange_account << "ȡ���˶������ս" << endl;
		}
	}
}

void gamer::rec_challange()
{
	system("cls");
	clock_t starttimer, stoptimer;
	
	char in_word[MAX_WORD_NUM + 1];
	char word[MAX_WORD_NUM + 1];
	char recvebuf[BUF_SIZE];
    char sendbuf[BUF_SIZE] = { "\0" };
	
	char cmd_str[BUF_SIZE];
	char cmd;
	if (whether == FALSE)
	{
		cout << "��ʱû����ս�����㷢����ս" << endl;
	}
	else
	{
		cout << "���������㷢����ս����ս����Ϣ" << endl;
		cout << "�˺�Ϊ��" << challange_account << " ";
		cout << "����Ϊ��" << challange_name << endl;
		cout << "�Ƿ����������--------Y      �˳�--------�������" << endl;
		cin >> cmd_str;

		if ((cmd_str[0] != 'Y' )&&( cmd_str[0] != 'y'))
		{
			cout << "�ɹ��˳�������ս�߽���" << endl;
		}
		else
		{
			int command;
			cout << "********************************************************" << endl;
			cout << "*                    ��ѡ�����                        *" << endl;
			cout << "*    1������ս        2�ܾ���ս          3�˳�         *" << endl;
			cout << "********************************************************" << endl;
			cin >> cmd_str;
			cmd = cmd_str[0];
			command = transfer_cmd(cmd);
			cout << "�ȴ�ϵͳȷ����..........." << endl;
			while (command != 3)
			{
				if (command == 1)
				{
					whether = 0;
					ZeroMemory(sendbuf, BUF_SIZE);
					sendbuf[0] = 'Y';
					send(v_client2, sendbuf, strlen(sendbuf), 0);

					ZeroMemory(recvebuf, BUF_SIZE);
					recv(client, recvebuf, BUF_SIZE, 0);//���յ���
					strcpy(word, recvebuf);
					system("cls");
					cout << "��ս��ʼ" << endl;
					cout << "�������ļ��������������" << endl << word;

					ZeroMemory(sendbuf, BUF_SIZE);
					sendbuf[0] = 'Y';
					send(v_client2, sendbuf, strlen(sendbuf), 0);//���յ����ʺ�������Ӧ

					ZeroMemory(recvebuf, BUF_SIZE);
					recv(v_client2, recvebuf, BUF_SIZE, 0);//������������������

					system("cls");
					cout << "������ղ�����ʾ����" << endl;
					starttimer = clock();
					char ch;
					cin.get(ch);
					cin.get(ch);
					int LetterNum;
					for (LetterNum = 0; (ch != '\n') && (LetterNum < MAX_WORD_NUM); LetterNum++)
					{
						in_word[LetterNum] = ch;
						cin.get(ch);
					}
					in_word[LetterNum] = '\0';
					if (strcomp(in_word, word) == TRUE)
					{
						stoptimer = clock();
						float time = ((double)(stoptimer - starttimer)) / CLK_TCK;
						time = time + 1;

						cout << "�ȴ�ϵͳ�б���..........." << endl;
						ZeroMemory(sendbuf, BUF_SIZE);
						memcpy(sendbuf, &time, 4);
						send(v_client2, sendbuf, strlen(sendbuf), 0);//������ʱ�䷢��ȥ
						ZeroMemory(recvebuf, BUF_SIZE);
						recv(v_client2, recvebuf, BUF_SIZE, 0);//����ʧ�ܻ��߳ɹ���ȷ��

						if (recvebuf[0] == 'N')                //�Է���սʧ��
						{
							int cur_experience = (int)(get_num()*(INC_PLAYER_EXPER_RATIO / (time - 1))) * 2;//����������ƽʱ������
							change(PLAYER, get_num(), cur_experience);
						}
						else                                    //�Է���ս�ɹ���
						{
							int cur_experience = (int)(get_num()*(INC_PLAYER_EXPER_RATIO / (time - 1))) * (-2);
							change(PLAYER, get_num(), cur_experience);//ʧ�ܺ󣬻�۳�ԭ������������
						}

						system("cls");
						if (recvebuf[0] == 'Y')
							cout << "�Է���ս�ɹ�" << endl;
						else
							cout << "�Է���սʧ��" << endl;
					}
					else
					{
						stoptimer = clock();
						float time = ((double)(stoptimer - starttimer)) / CLK_TCK;
						time = time + 1;

						cout << "�������" << endl;
						ZeroMemory(sendbuf, BUF_SIZE);//����������N��־����ȥ��
						sendbuf[0] = 'N';
						send(v_client2, sendbuf, strlen(sendbuf), 0);
						ZeroMemory(recvebuf, BUF_SIZE);
						recv(v_client2, recvebuf, BUF_SIZE, 0);//���նԷ���ս�Ƿ�ɹ���ȷ��

						if (recvebuf[0] == 'N')//�Է���սʧ��
						{
							int cur_experience = (int)(get_num()*(INC_PLAYER_EXPER_RATIO / (time - 1))) * 2;//����������ƽʱ������
							change(PLAYER, get_num(), cur_experience);
						}
						else                    //�Է���ս�ɹ���
						{
							int cur_experience = (int)(get_num()*(INC_PLAYER_EXPER_RATIO / (time - 1))) * (-2);
							change(PLAYER, get_num(), cur_experience);//ʧ�ܺ󣬻�۳�ԭ������������
						}
					}

					break;
				}
				else if (command == 2)
				{
					whether = 0;
					ZeroMemory(sendbuf, BUF_SIZE);
					sendbuf[0] = 'N';
					send(v_client2, sendbuf, strlen(sendbuf), 0);
					break;
				}
				system("cls");
				cout << "********************************************************" << endl;
				cout << "*                    ��ѡ�����                        *" << endl;
				cout << "*    1������ս        2�ܾ���ս          3�˳�         *" << endl;
				cout << "********************************************************" << endl;
				cin >> cmd_str;
				cmd = cmd_str[0];
				command = transfer_cmd(cmd);
				cout << "�ȴ�ϵͳȷ����..........." << endl;
			}
		}
	}
}

void gamer::do_challange(word_pool e_pool, word_pool m_pool, word_pool d_pool)
{
	challange_lab = TRUE;
	int command;
	char cmd;
	char cmd_str[MAX_ARRAY_NUM] = { '\0' };
	char copy_account[MAX_ARRAY_NUM] = { '\0' };
	char recvebuf[BUF_SIZE], sendbuf[BUF_SIZE] = { "\0" };
	clock_t starttimer, stoptimer;
	command = 1;

		insearch_logon(PLAYER);
		int in_command = DO_CHALLANGE;
		ZeroMemory(sendbuf, BUF_SIZE);
		memcpy(sendbuf,&in_command ,4);
		send(client, sendbuf, strlen(sendbuf), 0);
		ZeroMemory(recvebuf, BUF_SIZE);
		recv(client, recvebuf, BUF_SIZE, 0);

		cout << "��ѡ��������ս����ţ�����Ӣ�ġ�->������" << endl;
		cin >> copy_account;
		char *account = get_account();
		while (strcmp(copy_account, account) == 0)
		{
			cout << "���ܶ��Լ�������ս" << endl;
			cout << "��������,����Ӣ�ġ�->�����˳�" << endl;
			cin >> copy_account;
		}

		ZeroMemory(sendbuf, BUF_SIZE);
		strcpy(sendbuf,copy_account);
		send(client, sendbuf, strlen(sendbuf), 0);
		while (1)
		{ 
			ZeroMemory(recvebuf, BUF_SIZE);
			recv(client, recvebuf, BUF_SIZE, 0);
			if (recvebuf[0] == 'n')
			{
				int in_cmd;
				cout << "********************************************************" << endl;
				cout << "*                    ��ѡ�����                        *" << endl;
				cout << "*      1�ȴ��Է�Ӧ��             2�˳���ȡ����ս       *" << endl;
				cout << "********************************************************" << endl;
				cin >> cmd_str;
				cmd = cmd_str[0];
				in_cmd = transfer_cmd(cmd);
				cout << "�ȴ��Է�Ӧ����..........." << endl;
				if (in_cmd == 2)
				{
					ZeroMemory(sendbuf, BUF_SIZE);
					sendbuf[0] = 'N';
					send(client, sendbuf, strlen(sendbuf), 0);
					challange_lab = FALSE;
					system("cls");
					break;
				}
				else
				{
					ZeroMemory(sendbuf, BUF_SIZE);
					sendbuf[0] = 'Y';
					send(client, sendbuf, strlen(sendbuf), 0);
				}
			}
			else if (recvebuf[0] == 'N')
			{
				if ((copy_account[0] == '-') && (copy_account[1] == '>'))
				{
				}
				else if ((recvebuf[0] == 'N') && (recvebuf[1] == 'N') && (recvebuf[2] == 'N') && (recvebuf[3] == 'N'))
					cout << "�ô����߲�������" << endl;
				else if ((recvebuf[0] == 'N') && (recvebuf[1] == 'N') && (recvebuf[2] == 'N'))
					cout << "�����������ս������" << endl;
				else if ((recvebuf[0] == 'N') && (recvebuf[1] == 'N'))
					cout << "�б�����������ս�����" << endl;
				else
					cout << "�Է��ܾ�������ս," << endl;
				
				challange_lab = FALSE;
				break;
			}
			else
			{

				char **word = NULL;
				word = new char*[WORD_NUM];
				for (int i = 0; i < WORD_NUM; i++)
				{
					word[i] = new char[MAX_WORD_NUM + 1];
				}
				e_pool.rand_word(word, 0, 0);//�ӵ��ʳ���߽��ճ�һ�����ʳ�����

				ZeroMemory(sendbuf, BUF_SIZE);
				strcpy(sendbuf, word[0]);
				send(client, sendbuf, strlen(sendbuf), 0);//�Ѹõ��ʷ��͸�������
				system("cls");
				cout << "��ս��ʼ" << endl;
				cout << "�����ļ����±��������" << endl;
				cout << word[0];
				ZeroMemory(recvebuf, BUF_SIZE);
				recv(client, recvebuf, BUF_SIZE, 0);//�ȵط���������������

				system("cls");
				cout << "������ղ�����ʾ����" << endl;
				starttimer = clock();
				char ch;
				char in_word[MAX_WORD_NUM + 1];
				cin.get(ch);
				cin.get(ch);
				int LetterNum;
				for (LetterNum = 0; (ch != '\n') && (LetterNum < MAX_WORD_NUM); LetterNum++)
				{
					in_word[LetterNum] = ch;
					cin.get(ch);
				}                   //���뱾�صĵ�������
				in_word[LetterNum] = '\0';
				if (strcomp(in_word, word[0]) == TRUE)
				{
					stoptimer = clock();
					float time = ((double)(stoptimer - starttimer)) / CLK_TCK;
					time = time + 1;
					cout << "�ȴ�ϵͳ�б�........." << endl;
					ZeroMemory(sendbuf, BUF_SIZE);
					memcpy(sendbuf, &time, 4);
					send(client, sendbuf, strlen(sendbuf), 0);//������ʱ�䷢��ȥ

					ZeroMemory(recvebuf, BUF_SIZE);
					recv(client, recvebuf, BUF_SIZE, 0);//����ʧ�ܻ��߳ɹ���ȷ��
					if (recvebuf[0] == 'Y')
					{
						int cur_experience = (int)(get_num()*(INC_PLAYER_EXPER_RATIO / (time - 1))) * 2;//����������ƽʱ������
						change(PLAYER, get_num(), cur_experience);
					}
					else
					{
						int cur_experience = (int)(get_num()*(INC_PLAYER_EXPER_RATIO / (time - 1))) * (-2);
						change(PLAYER, get_num(), cur_experience);//ʧ�ܺ󣬻�۳�ԭ������������
					}

					if (recvebuf[0] == 'Y')
						cout << "��ս�ɹ�" << endl;
					else
						cout << "��սʧ��" << endl;
				}
				else
				{
					stoptimer = clock();
					float time = ((double)(stoptimer - starttimer)) / CLK_TCK;
					time = time + 1;

					cout << "�������" << endl;
					ZeroMemory(sendbuf, BUF_SIZE);//���������ı�־��N������ȥ��
					sendbuf[0] = 'N';
					send(client, sendbuf, strlen(sendbuf), 0);
					ZeroMemory(recvebuf, BUF_SIZE);
					recv(client, recvebuf, BUF_SIZE, 0);//���նԷ���ս�Ƿ�ɹ���ȷ��

					int cur_experience = (int)(get_num()*(INC_PLAYER_EXPER_RATIO / (time-1))) * (-2);
					change(PLAYER, get_num(), cur_experience);//ʧ�ܺ󣬻�۳�ԭ������������
				}
				challange_lab = FALSE;
				for (int k = 0; k < WORD_NUM; k++)
				{
					delete [] word[k];
				}
				break;
			}
		}
		challange_lab = FALSE;
}