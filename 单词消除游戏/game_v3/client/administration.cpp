#include <Winsock2.h>
#include<iostream>
#include<fstream>
#include<string>
#include<iomanip>
#include<windows.h>
#include"mylib.h"
#include"individual.h"
#include"wordpool.h"
#include"administration.h"
#pragma comment(lib,"ws2_32.lib")
using namespace std;

void administrator::set_question(int role, 
	                            string e_question,string m_question,string d_question,
								word_pool e_pool,word_pool m_pool,word_pool d_pool)
{
	int command;
	system("cls");
	cout << "********************************************************" << endl;
	cout << "*                  ��ѡ�����                          *" << endl;
	cout << "*     1.��ʼ����                2.����������˳���     *" << endl;
	cout << "********************************************************" << endl;
	char cmd_str[MAX_ARRAY_NUM];
	char cmd;
	cin >> cmd_str;
	cmd = cmd_str[0];
	command = transfer_cmd(cmd);
	
	clock_t start_time, stop_time;
	double duration=0;

	while (command != 2)
	{
		int question_num = 0;
		string cur_word;
		if (1 == command)
		{
			int in_command = 1;
			fstream questionFile1(e_question, ios::out | ios::in);
			questionFile1.seekp(-1,ios::end);

			fstream questionFile2(m_question, ios::out | ios::in);
			questionFile2.seekp(-1,ios::end);

			fstream questionFile3(d_question, ios::out | ios::in);
			questionFile3.seekp(-1,ios::end);                          //��������ͬ���׵Ĵʿ�

			while (in_command != 2)
			{
				system("cls");
				if (1 == in_command)
				{
					start_time = clock();
					cout << "��������Ҫ���ӵĵ���("<<MAX_WORD_NUM<<"����ĸ����)" << endl;

					char cur_word[MAX_WORD_NUM + 1];
					char ch1,ch;
					cin.get(ch1);
					cin.get(ch);
					int LetterNum;
					for (LetterNum = 0; (ch != '\n') && (LetterNum<MAX_WORD_NUM); LetterNum++)
					{
						cur_word[LetterNum] = ch;
						cin.get(ch);
					}                      //���������ĵ��ʽ��ж���
					cur_word[LetterNum] = '\0';

					//ͨ��������ĸ�������ж��������ֿ⡣���������
					if (LetterNum <= EASY)
					{
						int i = e_pool.insert_pool(cur_word);
						if (i == TRUE)
						{
							questionFile1 << setiosflags(ios::left) << setw(EASY) << setfill(' ') << cur_word << " "<<" ";
							cout << "����ɹ�" << endl;
							question_num++;
						}
						else
							cout << "����ʧ��"<<endl;
					}
					else if (LetterNum <= MEDIUM)
					{
						int i = m_pool.insert_pool(cur_word);
						if (i == TRUE)
						{
							questionFile2 << setiosflags(ios::left) << setw(MEDIUM) << setfill(' ') << cur_word << " " << " ";
							cout << "����ɹ�" << endl;
							question_num++;
						}
						else
							cout << "����ʧ��"<<endl;
					}
					else
					{
						int i = d_pool.insert_pool(cur_word);
						if (i == TRUE)
						{
							questionFile3 << setiosflags(ios::left) << setw(DIFFICULT) << setfill(' ') << cur_word << " " << " ";
							cout << "����ɹ�" << endl;
							question_num++;
						}
						else
							cout << "����ʧ��"<<endl;
					}

					stop_time = clock();
					duration = duration + ((double)(stop_time - start_time)) / CLK_TCK;//�����������ʱ�䣬Ϊ���±߼��㾭��
				}

				cout << "********************************************************" << endl;
				cout << "*                  ��ѡ�����                          *" << endl;
				cout << "*       1.����                          2.�˳�         *" << endl;
				cout << "********************************************************" << endl;
				cin >> cmd_str;
				cmd = cmd_str[0];
				in_command = transfer_cmd(cmd);
				
			}
			questionFile1 << " ";
			questionFile1.close();
			questionFile2 << " ";
			questionFile2.close();
			questionFile3 << " ";
			questionFile3.close();
			//���������д��ո���Ϊ���Զ�����ֿ���ͨ���ո�ĸ������ж��ļ�������
			int cur_experience = 0;
			int word_num = get_num() + question_num;
			cur_experience = (int) (word_num+1) * (INC_SETQUE_EXPER_RATIO / duration);
			//���㾭�飨ͨ��ʱ�䡢Ŀǰ�����ĵ������Լ������߾�������ϵ����INC_SETQUE_EXPER_RATIO������������ʵ�֣�
			change(SET_QUE_MAN, get_num() + question_num,cur_experience);
		}
		system("cls");
		cout << "********************************************************" << endl;
		cout << "*                  ��ѡ�����                          *" << endl;
		cout << "*     1.��ʼ����                2.����������˳���     *" << endl;
		cout << "********************************************************" << endl;
		cin >> cmd_str;
		cmd = cmd_str[0];
		command = transfer_cmd(cmd);
	
	}
}

void administrator::adm_operation(int role,
	                             string e_question, string m_question, string d_question,
	                             word_pool e_pool, word_pool m_pool, word_pool d_pool)
{
	int out_command;
	system("cls");
	cout << "********************************************************" << endl;
	cout << "*                       ��ѡ�����                     *" << endl;
	cout << "*       "<<REGISTER<<".ע��           "<<LOGIN<<".��½            3.�˳�      *" << endl;
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
			reg_back = init_operate(REGISTER, role); break;//ע��
		case 2:
		{
			int login_back = init_operate(LOGIN, role);
			if (login_back == TRUE)    //��½�ɹ��󣬽�����ز���
			{
				int in_command;
				system("cls");
				cout << "********************************************************" << endl;
				cout << "*                      ��ѡ�����                      *" << endl;
				cout << "*       1����          2�������ѯ           3.�˳�    *" << endl;
				cout << "********************************************************" << endl;
				cin >> cmd_str;
				cmd = cmd_str[0];
				in_command = transfer_cmd(cmd);
				
				while (in_command != 3)
				{
					switch (in_command)
					{
					case 1:
						set_question(role, e_question,m_question,d_question,e_pool,m_pool,d_pool); 
					  break;

					case 2:operate(role); break;
					default:break;
					}
					system("cls");
					cout << "********************************************************" << endl;
					cout << "*                      ��ѡ�����                      *" << endl;
					cout << "*       1����          2�������ѯ           3.�˳�    *" << endl;
					cout << "********************************************************" << endl;
					cin >> cmd_str;
					cmd = cmd_str[0];
					in_command = transfer_cmd(cmd);
				}
				if (in_command == 3)
				{
					int command;
					char recvebuf[BUF_SIZE], sendbuf[BUF_SIZE] = { "\0" };
					ZeroMemory(sendbuf, BUF_SIZE);       
					command = BACK;
					memcpy(sendbuf, &command, 4);
					int retVal = send(client, sendbuf, strlen(sendbuf), 0);//������������˳��˻�������
					
					ZeroMemory(recvebuf, BUF_SIZE);
					recv(client, recvebuf, BUF_SIZE, 0);// ���շ������˵�ȷ�ϣ�
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
		
	}
}
