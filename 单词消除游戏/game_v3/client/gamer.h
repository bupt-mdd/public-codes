using namespace std; 

class gamer :public individual
{
private:
	char challange_account[PROPER_NUM] ;   //��¼��ս���˺�
	char challange_name[PROPER_NUM];      //��¼��ս������
	int whether;         
	int challange_lab;    //��������־��¼����ҵ�ǰ�Ƿ񱻱�����ս�Լ��Ƿ���ս����

	void run_game(int role,  word_pool e_pool, word_pool m_pool, word_pool d_pool, int pass_num);
	void play_game(int role,  word_pool e_pool, word_pool m_pool, word_pool d_pool );
	//����Ϸģ��
public:
	gamer();
	~gamer();
	void rec_challange();          //������սģ��
	void do_challange(word_pool e_pool, word_pool m_pool, word_pool d_pool);//������սģ��
	void gamer_operation(int role,  word_pool e_pool, word_pool m_pool, word_pool d_pool);
	void listen();//�����Ƿ�����ս��ģ��
};
