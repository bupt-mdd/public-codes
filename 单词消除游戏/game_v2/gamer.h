using namespace std; 

class gamer :public individual
{
private:
	void run_game(int role, string player_inf, string adm_inf, word_pool e_pool, word_pool m_pool, word_pool d_pool, int pass_num);
	void play_game(int role, string player_inf, word_pool e_pool, word_pool m_pool, word_pool d_pool, string adm_inf);
    //�����߽�������к���ҵĴ��ز���
public:
	void gamer_operation(int role, string player_inf, string  adm_inf, word_pool e_pool, word_pool m_pool, word_pool d_pool);
};
