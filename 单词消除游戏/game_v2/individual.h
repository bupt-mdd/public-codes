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
	string game_account;                             //�˻���
	string user_name;                                //�������
	string user_password;                            //�û�����
	int sort_standard;                               //�Ƚ�ʱ�ı�׼
	int user_rank;                                   //��ҵȼ�
	int user_experience;                             //��Ҿ���
	int que_or_passnum;                              //���������߳�����
	void change_username(string cur_inf);            //�޸�����
	void change_password(string cur_inf);            //�޸�����
	int user_register(string cur_inf);               //���ע��
	int user_login(string cur_inf);                  //��ҵ�½
	int account_search(char find_str[],string cur_inf);//���˺Ų�ѯ�����Ϣ
	int name_search(char find_str[], string cur_inf);//��������ѯ�����Ϣ
	int rank_search(int find_int, string cur_inf);//���ȼ���ѯ�����Ϣ
	int exp_search(int find_int, string cur_inf);//�������ѯ�����Ϣ
	int num_search(int find_int,string cur_inf);//�����������߳�������ѯ�����Ϣ
	void search_All_individual(int role, string player_inf, string  adm_inf);//��ѯ������ҵ���Ϣ
	void search_individual(int role, string player_inf, string  adm_inf);//�����Բ�ѯ�����Ϣ
	
	void merge(individual *&Arrayptr, individual *&Arrayptr_copy, int left, int q, int right);
	void merge_pass(individual *&Arrayptr, individual *&Arrayptr_1, int s, int num);
	void merge_sort(individual *&Arrayptr, int num);
	void show_result(individual *Arrayptr, int num);
	void sort( string player_inf, string  adm_inf);
	//�ϲ������㷨ʵ�������Ϣ������������
public:
	int get_num() { return que_or_passnum; };   //�õ����������ߴ�����
	void change(int role, string player_inf, string adm_inf, int pass_num,int cur_experience);//�ı侭��ȼ���
	int init_operate(int command, int role, string player_inf, string adm_inf);//���õ�½��ע�ắ��
	void operate(int role, string player_inf, string  adm_inf);
	individual();
	individual(string& account, string& name, string& password, int experience, int standard, int rank, int num);
	individual(const individual& I);
};
