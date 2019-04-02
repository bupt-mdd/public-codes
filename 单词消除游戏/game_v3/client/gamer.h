using namespace std; 

class gamer :public individual
{
private:
	char challange_account[PROPER_NUM] ;   //记录挑战者账号
	char challange_name[PROPER_NUM];      //记录挑战者姓名
	int whether;         
	int challange_lab;    //者两个标志记录该玩家当前是否被别人挑战以及是否挑战别人

	void run_game(int role,  word_pool e_pool, word_pool m_pool, word_pool d_pool, int pass_num);
	void play_game(int role,  word_pool e_pool, word_pool m_pool, word_pool d_pool );
	//玩游戏模块
public:
	gamer();
	~gamer();
	void rec_challange();          //接收挑战模块
	void do_challange(word_pool e_pool, word_pool m_pool, word_pool d_pool);//发起挑战模块
	void gamer_operation(int role,  word_pool e_pool, word_pool m_pool, word_pool d_pool);
	void listen();//监听是否有挑战的模块
};
