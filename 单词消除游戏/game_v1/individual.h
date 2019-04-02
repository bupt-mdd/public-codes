# define MAXNUM_STR 160
# define PROPER_NUM 20
# define REGISTER 2
# define PLAYER 1
# define SET_MAN 2
# define SET_QUE_MAN 2
# define TRUE 1
# define FALSE 0
# define WORD_NUM 5                  //��������
# define WAIT_TIME 5
# define MAX_ARRAY_NUM 200
using namespace std;

int transfer_cmd(char *command); 

class individual
{
private:
	string game_account;              //����˺�
	string user_name;                 //�������
	string user_password;             //�������
	int sort_standard;                //�Ƚϵı�׼
	int user_rank;                    //��ҵȼ�
	int user_experience;              //��Ҿ���
	int que_or_passnum;               //��ҳ��������ߴ�����
	void change_username(string cur_inf);//�޸�����
	void change_password(string cur_inf);//�޸�����
	int user_register(string cur_inf);//���ע��
	int user_login(string cur_inf);//��ҵ�½
	int account_search(char find_str[], string cur_inf);//�����˻���ѯ
	int name_search(char find_str[], string cur_inf);//����������ѯ
	int rank_search(int find_int, string cur_inf);//���յȼ���ѯ
	int exp_search(int find_int, string cur_inf);//���վ����ѯ
	int num_search(int find_int, string cur_inf);//���ճ����������ߴ�������ѯ
	void search_All_individual(int role, string player_inf, string  adm_inf);//��ѯ������ҵ���Ϣ
	void search_individual(int role, string player_inf, string  adm_inf);
	void merge(individual *&Arrayptr, individual *&Arrayptr_copy, int left, int q, int right);
	void merge_pass(individual *&Arrayptr, individual *&Arrayptr_1, int s, int num);
	void merge_sort(individual *&Arrayptr, int num);
	void show_result(individual *Arrayptr, int num);
	void sort( string player_inf, string  adm_inf);
	//ʹ�úϲ������㷨ʵ�������Ϣ�������Խ�������
public:
	int get_num() { return que_or_passnum; };//��õ����˻��ĳ������ʹ�����
	void change_que_or_passnum(int role, string player_inf, string adm_inf, int num);
	//�ôʺ���ʵ�ֹؿ����޸ĺͳ��������޸ġ�
	int init_operate(int command, int role, string player_inf, string adm_inf);//ͨ������������õ�¼��ע�ắ��
	void operate(int role, string player_inf, string  adm_inf);
	individual();
	individual(string& account, string& name, string& password, int experience, int standard, int rank, int num);
	individual(const individual& I);
};
