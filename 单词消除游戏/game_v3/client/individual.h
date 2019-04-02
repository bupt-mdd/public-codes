using namespace std;

class individual
{
private:
	char game_account[PROPER_NUM];          //�˺���
	char user_name[PROPER_NUM];             //�������        
	char user_password[PROPER_NUM];         //�������
	int sort_standard;                      //�����׼��Ϊ�˷���������Ϣ����ͬ�ı�׼��������
	int user_rank;                          //��ҵȼ�
	int user_experience;                    //��Ҿ���
	int que_or_passnum;                     //��ҵĴ��������߳�����
	void change_username();                 //�޸�����
	void change_password();                 //�޸�����
	int user_register(int role);            //���ע��
	int user_login(int role);               //��ҵ�½
	void search_All_individual();           //��ѯ������е����
	void search_individual();               
	void search(int num);                   //�����Բ�ѯ�����Ϣ

	void merge(individual *&Arrayptr, individual *&Arrayptr_copy, int left, int q, int right);
	void merge_pass(individual *&Arrayptr, individual *&Arrayptr_1, int s, int num);
	void merge_sort(individual *&Arrayptr, int num);
	void show_result(individual *Arrayptr, int num);
	void sort();
	//�ϲ������㷨ʵ�������Ϣ���������
public:

	int client;
	int v_client1;
	int v_client2;              //�������������socketͨ�нӿ�

	void insearch_logon(int _role);
	void search_log();
	int get_num() { return que_or_passnum; };     //�õ����������ߴ�����
	char *get_account(){ return game_account; };   //�õ��˺���
	void change(int role, int pass_num,int cur_experience);//

	int init_operate(int command, int role);//ͨ���������������������ø���˽�к���
	void operate(int role);
	
	individual();
	individual(char *account, char *name, char *password, int experience, int standard, int rank, int num, int _client, int _v_client1,int _v_client2);
	individual(const individual& I);
};
