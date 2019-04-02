using namespace std;

class work
{
private:

	string e_question;
	string m_question;
	string d_question;

	word_pool e_pool;    //（easy）简单单词的单词池
	word_pool m_pool;    //（medium）中等单词的单词池
	word_pool d_pool;    //（difficult）困难单词的单词池

public:

	gamer player;
	administrator set_question;
	void set_work();
	void run_client();
	work();
	~work();
};