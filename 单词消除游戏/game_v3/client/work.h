using namespace std;

class work
{
private:

	string e_question;
	string m_question;
	string d_question;

	word_pool e_pool;    //��easy���򵥵��ʵĵ��ʳ�
	word_pool m_pool;    //��medium���еȵ��ʵĵ��ʳ�
	word_pool d_pool;    //��difficult�����ѵ��ʵĵ��ʳ�

public:

	gamer player;
	administrator set_question;
	void set_work();
	void run_client();
	work();
	~work();
};