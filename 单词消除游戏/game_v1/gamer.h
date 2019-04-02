using namespace std; 

class gamer :public individual
{
private:
	void run_game(int role, string player_inf, string question, string adm_inf, int pass_num);
	void play_game(int role, string player_inf, string question, string adm_inf);//ÍæÓÎÏ·Ä£¿é
public:
	void gamer_operation(int role, string player_inf, string  adm_inf, string question);
};
