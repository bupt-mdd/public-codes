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
	int insert_pool(char *in);     //����ϣ���в���һ������
	void build_pool(int filetype, string filename1, string filename2, string filename3);//�����ϣ��
	void rand_word(char **&wordptr, int startnum, int stopnum);//�ӹ�ϣ���������������stopnum-startnum+1��������
	word_pool();
	~word_pool();
};

