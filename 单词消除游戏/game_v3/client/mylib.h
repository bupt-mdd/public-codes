# define MAXNUM_STR 160
# define PROPER_NUM 20     
# define PLAYER 1
# define SET_MAN 2
# define SET_QUE_MAN 2
# define TRUE 1
# define FALSE 0
# define WORD_NUM 2
# define INC_RANK_RATIO 10                 //等级增长系数
# define INC_PLAYER_EXPER_RATIO 10         //闯关者经验增长系数
# define INC_SETQUE_EXPER_RATIO 20         //出题者经验增长系数
# define WAIT_TIME 5                       //单词显示时间
# define MAX_ARRAY_NUM 200
# define EASY 7
# define DIFFICULT 40
# define MEDIUM 11
# define BUF_SIZE 50                       //与服务器交互时，缓冲数组的长度
# define CHANGE_NAME 8
# define CHANGE_PASSWORD 3
# define REGISTER 1
# define LOGIN 2
# define SEARCH_ALL 4
# define SEARCH_ONES 5
# define SORT 6
# define CHANGE 7
# define BACK 9
# define END_BACK 10
# define LOG_OUT 11
# define REC_CHALLANGE 12
# define DO_CHALLANGE 14
# define SEARCH_LOG 13                     //各种操作命令
# define MAX_WORD_NUM 40

extern int listen_lab;            //监听对方挑战的标志
extern int close;                  //关闭程序标志
extern void listen1(void* lpParameter);    //监听函数
extern void run(void* lpParameter);
int transfer_cmd(char command);
