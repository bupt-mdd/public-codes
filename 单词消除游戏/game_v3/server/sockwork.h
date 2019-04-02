
class sockwork
{
private:
	int role;
	char game_account[PROPER_NUM];
	char user_name[PROPER_NUM];
	char user_password[PROPER_NUM];
	int sort_standard;
	int user_rank;
	int user_experience;
	int que_or_passnum;
	void change_username();
	void change_password();
	void user_register();
	void user_login();
	void search_All_individual();
	void search_individual();
	void sort();
	void change();
	void back();
	void search_log();
	void challange();
	void account_search(char find_str[], string cur_inf);
	void name_search(char find_str[], string cur_inf);
	void rank_search(int find_int, string cur_inf);
	void exp_search(int find_int, string cur_inf);
	void num_search(int find_int, string cur_inf);
public:
	SOCKET	mysock;
	SOCKET	v_mysock1;
	SOCKET	v_mysock2;

	sockwork();
	sockwork(char *account, char *name, char *password, int experience, int standard, int rank, int num, int _role, int _sock, int _v_mysock1, int _v_mysock2);
	sockwork(const sockwork& I);
	void setSock(SOCKET	client, SOCKET	v_client1,SOCKET	v_client2 )
	{
		mysock = client;
		v_mysock1 = v_client1;
		v_mysock2 = v_client2;
	}
	void work();
};