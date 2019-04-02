# define MAX_WORD_NUM 40           //单词的最大字母个数
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
	int insert_pool(char *in);                    //将一个单词插入到单词池中
	void build_pool(int filetype, string filename1, string filename2, string filename3);//建造单词池
	void rand_word(char **&wordptr, int startnum, int stopnum);//随机从单词池中挑选（stopnum-startnum）个单词出来
	word_pool();
	~word_pool();
};

