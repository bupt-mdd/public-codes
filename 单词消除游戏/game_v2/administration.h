using namespace std;

class administrator :public individual
{
private:
	void set_question(int role,
		              string player_inf, string  adm_inf,
		              string e_question, string m_question, string d_question,
					  word_pool e_pool, word_pool m_pool, word_pool d_pool);
	//出题模块
public:
	void adm_operation(int role,
		               string player_inf, string  adm_inf,
		               string e_question, string m_question, string d_question,
					   word_pool e_pool, word_pool m_pool, word_pool d_pool);
	//其他查询操作模块
};