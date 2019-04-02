# define MAXNUM_STR 160
# define PROPER_NUM 20
# define REGISTER 2
# define PLAYER 1
# define SET_MAN 2
# define SET_QUE_MAN 2
# define TRUE 1
# define FALSE 0
# define WORD_NUM 5                  //各种命令
# define WAIT_TIME 5
# define MAX_ARRAY_NUM 200
using namespace std;

int transfer_cmd(char *command); 

class individual
{
private:
	string game_account;              //玩家账号
	string user_name;                 //玩家姓名
	string user_password;             //玩家密码
	int sort_standard;                //比较的标准
	int user_rank;                    //玩家等级
	int user_experience;              //玩家经验
	int que_or_passnum;               //玩家出题数或者闯关数
	void change_username(string cur_inf);//修改姓名
	void change_password(string cur_inf);//修改密码
	int user_register(string cur_inf);//玩家注册
	int user_login(string cur_inf);//玩家登陆
	int account_search(char find_str[], string cur_inf);//按照账户查询
	int name_search(char find_str[], string cur_inf);//按照姓名查询
	int rank_search(int find_int, string cur_inf);//按照等级查询
	int exp_search(int find_int, string cur_inf);//按照经验查询
	int num_search(int find_int, string cur_inf);//按照出题算数或者闯关数查询
	void search_All_individual(int role, string player_inf, string  adm_inf);//查询所欲玩家的信息
	void search_individual(int role, string player_inf, string  adm_inf);
	void merge(individual *&Arrayptr, individual *&Arrayptr_copy, int left, int q, int right);
	void merge_pass(individual *&Arrayptr, individual *&Arrayptr_1, int s, int num);
	void merge_sort(individual *&Arrayptr, int num);
	void show_result(individual *Arrayptr, int num);
	void sort( string player_inf, string  adm_inf);
	//使用合并排序算法实现玩家信息按照属性进行排序
public:
	int get_num() { return que_or_passnum; };//获得当个账户的出题数和闯关数
	void change_que_or_passnum(int role, string player_inf, string adm_inf, int num);
	//用词函数实现关卡的修改和出题数的修改。
	int init_operate(int command, int role, string player_inf, string adm_inf);//通过这个函数调用登录和注册函数
	void operate(int role, string player_inf, string  adm_inf);
	individual();
	individual(string& account, string& name, string& password, int experience, int standard, int rank, int num);
	individual(const individual& I);
};
