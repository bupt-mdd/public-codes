# define MAXNUM_STR 160
# define PROPER_NUM 20
# define REGISTER 2
# define PLAYER 1
# define SET_MAN 2
# define SET_QUE_MAN 2
# define TRUE 1
# define FALSE 0
# define WORD_NUM 2
# define INC_RANK_RATIO 10
# define INC_PLAYER_EXPER_RATIO 10
# define INC_SETQUE_EXPER_RATIO 20
# define WAIT_TIME 5
# define MAX_ARRAY_NUM 200
# define EASY 7
# define DIFFICULT 40
# define MEDIUM 11
using namespace std;

int transfer_cmd(char *command);

class individual
{
private:
	string game_account;                             //账户名
	string user_name;                                //玩家姓名
	string user_password;                            //用户密码
	int sort_standard;                               //比较时的标准
	int user_rank;                                   //玩家等级
	int user_experience;                             //玩家经验
	int que_or_passnum;                              //闯关数或者出题数
	void change_username(string cur_inf);            //修改姓名
	void change_password(string cur_inf);            //修改密码
	int user_register(string cur_inf);               //玩家注册
	int user_login(string cur_inf);                  //玩家登陆
	int account_search(char find_str[],string cur_inf);//按账号查询玩家信息
	int name_search(char find_str[], string cur_inf);//按姓名查询玩家信息
	int rank_search(int find_int, string cur_inf);//按等级查询玩家信息
	int exp_search(int find_int, string cur_inf);//按经验查询玩家信息
	int num_search(int find_int,string cur_inf);//按闯关数或者出题数查询玩家信息
	void search_All_individual(int role, string player_inf, string  adm_inf);//查询所有玩家的信息
	void search_individual(int role, string player_inf, string  adm_inf);//按属性查询玩家信息
	
	void merge(individual *&Arrayptr, individual *&Arrayptr_copy, int left, int q, int right);
	void merge_pass(individual *&Arrayptr, individual *&Arrayptr_1, int s, int num);
	void merge_sort(individual *&Arrayptr, int num);
	void show_result(individual *Arrayptr, int num);
	void sort( string player_inf, string  adm_inf);
	//合并排序算法实现玩家信息按照属性排序
public:
	int get_num() { return que_or_passnum; };   //得到出题数或者闯关数
	void change(int role, string player_inf, string adm_inf, int pass_num,int cur_experience);//改变经验等级等
	int init_operate(int command, int role, string player_inf, string adm_inf);//调用登陆和注册函数
	void operate(int role, string player_inf, string  adm_inf);
	individual();
	individual(string& account, string& name, string& password, int experience, int standard, int rank, int num);
	individual(const individual& I);
};
