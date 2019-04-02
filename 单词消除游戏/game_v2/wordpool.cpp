#include<iostream>
#include<string>
#include<fstream>
#include<time.h>
#include"individual.h"
#include"wordpool.h"
using namespace std;

int strcomp(char *ch1, char *ch2)
{
	for (int i = 0; (ch1[i] != '\0') || (ch2[i] != '\0'); )
	{
		if (ch1[i] == ch2[i])
			i++;
		else
			return FALSE;
	}
	return TRUE;
}
//自定义比较函数
void copystr(char des[], char sour[])
{
	int i = 0;
	for (i = 0; sour[i] != '\0'; i++)
	{
		des[i] = sour[i];
	}
	des[i] = '\0';
}
//自定义拷贝函授

wordnode::wordnode(char *in)
{
	copystr(word, in);
	next = NULL;
}

wordlist::wordlist()
{
	ele_num = 0;
	head = next = NULL;
}

wordlist::~wordlist()
{
	wordnode *temp;
	while (head != NULL)
	{
		temp = head;
		head = head->next;
		delete temp;
	}
}

int wordlist::appendlist(char *in)
{
	if (ele_num == 0)
	{
		wordnode *new_word = new wordnode(in);
		head = new_word;
		head->next = NULL;
		ele_num++;
		return TRUE;
	}
	else
	{
		wordnode *temp = head;
		for (; temp != NULL; temp = temp->next)
		{
			if (strcomp(temp->word, in) == TRUE)
			{
				//cout << temp->word;
				return FALSE;
			}
		}
		wordnode *new_word = new wordnode(in);
		new_word->next = head->next;
		head->next = new_word;
		ele_num++;
		return TRUE;
	}
}

word_pool::word_pool()
{
	elem = new wordlist[52];
}

word_pool::~word_pool()
{
	//delete[]elem;
}

int word_pool::insert_pool(char *in)
{
	int i = (int)in[0];
	if (in[0] >= 'a')
		i = i - 97 + 26;
	else
		i = i - 65;
	return elem[i].appendlist(in);
}

void word_pool::build_pool(int filetype, string filename1, string filename2, string filename3)
{                        //分别从不同的字库中读取单词，并建立单词池
	char word_array[MAX_WORD_NUM + 1] = { '\0' };
	if (filetype == EASY)
	{
		char word_array[MAX_WORD_NUM + 1] = { '\0' };
		ifstream questionFile1(filename1);
		
		char ch = '\0';
		questionFile1.get(ch);
		int i = 0;
		while (ch != ' ')
		{
			questionFile1.seekg(i, ios::beg);
			char ch1, ch2;
			questionFile1.get(ch1);
			questionFile1.get(ch2);
			int j = 0;

			for (j = 0; (ch1 != ' ') || (ch2 != ' '); j++)
			{
				word_array[j] = ch1;
				ch1 = ch2;
				questionFile1.get(ch2);
			}
			word_array[j] = '\0';
			int p = insert_pool(word_array);
			i = i + (EASY + 2);
			questionFile1.seekg(i, ios::beg);
			questionFile1.get(ch);
		}
		questionFile1.close();
	}
	else if (filetype == DIFFICULT)
	{
		ifstream questionFile1(filename3);
		char ch = '\0';

		questionFile1.get(ch);
		int i = 0;
		while (ch != ' ')
		{
			questionFile1.seekg(i, ios::beg);
			char ch1, ch2;
			questionFile1.get(ch1);
			questionFile1.get(ch2);
			int j = 0;

			for (j = 0; (ch1 != ' ') || (ch2 != ' '); j++)
			{
				word_array[j] = ch1;
				ch1 = ch2;
				questionFile1.get(ch2);
			}
			word_array[j] = '\0';
			int p = insert_pool(word_array);
			i = i + (DIFFICULT + 2);
			questionFile1.seekg(i, ios::beg);
			questionFile1.get(ch);
		}
		questionFile1.close();
	}
	else
	{
		ifstream questionFile1("easy.txt");
		char ch = '\0';

		questionFile1.get(ch);
		int i = 0;
		while (ch != ' ')
		{
			questionFile1.seekg(i, ios::beg);
			char ch1, ch2;
			questionFile1.get(ch1);
			questionFile1.get(ch2);
			int j = 0;

			for (j = 0; (ch1 != ' ') || (ch2 != ' '); j++)
			{
				word_array[j] = ch1;
				ch1 = ch2;
				questionFile1.get(ch2);
			}
			word_array[j] = '\0';
			int p = insert_pool(word_array);
			i = i + (MEDIUM + 2);
			questionFile1.seekg(i, ios::beg);
			questionFile1.get(ch);
		}
		questionFile1.close();

	}
}

void word_pool::rand_word(char **&wordptr, int startnum, int stopnum)
{
	srand(time(NULL));
	int lab[52];
	for (int i = 0; i < 52; ++i) lab[i] = i;
	//for (int i = 0; i < 52; ++i) cout<<lab[i] <<endl;
	for (int i = 51; i > 0; --i) swap(lab[i], lab[rand() % i]);
	//for (int i = 0; i < 52; ++i) cout<<lab[i] <<endl;
	int j = 0;
	int rand_i = 0;
	for (int i = 0; i < (stopnum - startnum + 1); i++, rand_i++)
	{
		if (rand_i>51)
		{
			rand_i = 0;
		}
		j = lab[rand_i];
		srand(time(NULL));
		while (elem[j].head == NULL)
		{
			rand_i++;
			if (rand_i>51)
			{
				rand_i = 0;
			}
			j = lab[rand_i];
		}
		int k = rand() % elem[j].ele_num;
		wordnode *temp = elem[j].head;
		for (int n = 0; n < k; n++, temp = temp->next)
		{
		}
		copystr(wordptr[startnum + i], temp->word);
	}
}               //随机挑选给定个数的单词