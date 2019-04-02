# define MAX_WORD_NUM 40           //���ʵ������ĸ����
using namespace std;

int strcomp(char *ch1, char *ch2);
void copystr(char des[], char sour[]);

class wordnode
{
public:
	char word[MAX_WORD_NUM+1];
	wordnode *next;
	wordnode(char *in);
};

class wordlist
{
public:
	int ele_num;
	wordnode *head;
	wordnode *next;
	int appendlist(char *in);
	wordlist();
	~wordlist();
};

class word_pool
{
public:
	wordlist *elem;
	int insert_pool(char *in);                    //��һ�����ʲ��뵽���ʳ���
	void build_pool(int filetype, string filename1, string filename2, string filename3);//���쵥�ʳ�
	void rand_word(char **&wordptr, int startnum, int stopnum);//����ӵ��ʳ�����ѡ��stopnum-startnum�������ʳ���
	word_pool();
	~word_pool();
};

