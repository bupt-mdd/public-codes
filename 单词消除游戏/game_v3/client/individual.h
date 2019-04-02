using namespace std;

class individual
{
private:
	char game_account[PROPER_NUM];          //账号名
	char user_name[PROPER_NUM];             //玩家姓名        
	char user_password[PROPER_NUM];         //玩家密码
	int sort_standard;                      //排序标准。为了方便对玩家信息按不同的标准进行排序
	int user_rank;                          //玩家等级
	int user_experience;                    //玩家经验
	int que_or_passnum;                     //玩家的闯关数或者出题数
	void change_username();                 //修改姓名
	void change_password();                 //修改密码
	int user_register(int role);            //玩家注册
	int user_login(int role);               //玩家登陆
	void search_All_individual();           //查询输出所有的玩家
	void search_individual();               
	void search(int num);                   //暗属性查询玩家信息

	void merge(individual *&Arrayptr, individual *&Arrayptr_copy, int left, int q, int right);
	void merge_pass(individual *&Arrayptr, individual *&Arrayptr_1, int s, int num);
	void merge_sort(individual *&Arrayptr, int num);
	void show_result(individual *Arrayptr, int num);
	void sort();
	//合并排序算法实现玩家信息的排序输出
public:

	int client;
	int v_client1;
	int v_client2;              //与服务器建立的socket通行接口

	void insearch_logon(int _role);
	void search_log();
	int get_num() { return que_or_passnum; };     //得到出题数或者闯关数
	char *get_account(){ return game_account; };   //得到账号名
	void change(int role, int pass_num,int cur_experience);//

	int init_operate(int command, int role);//通过以下这两个函数来调用各个私有函数
	void operate(int role);
	
	individual();
	individual(char *account, char *name, char *password, int experience, int standard, int rank, int num, int _client, int _v_client1,int _v_client2);
	individual(const individual& I);
};
