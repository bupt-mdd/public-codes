using namespace std;

class administrator :public individual
{
private:
	void set_question(int role,
		              string e_question, string m_question, string d_question,
					  word_pool e_pool, word_pool m_pool, word_pool d_pool);//����ģ��
public:
	void adm_operation(int role,
		               string e_question, string m_question, string d_question,
					   word_pool e_pool, word_pool m_pool, word_pool d_pool);//�����Ϣ���õ�ģ��
};