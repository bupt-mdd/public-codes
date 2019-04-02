# define CHANGE_NAME 8
# define WAIT_TIME 5
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
# define SEARCH_LOG 13                                 //各种命令标志，与客户端实现了命令的统一
# define BUF_SIZE 50
# define SET_QUE_MAN 2
# define PLAYER 1
# define PROPER_NUM 20
# define MAXNUM_STR 160
# define INC_RANK_RATIO 10               //等级增长系数
# define INC_PLAYER_EXPER_RATIO 10       //闯关者经验增长系数
# define INC_SETQUE_EXPER_RATIO 20       //出题者经验增长系数
# define MAX_CLIENT 40                   //可同时进行连接的客户端个数，可通过修改该值来增加和减少所连的客户端
using namespace std;

extern char all_sendbuf[BUF_SIZE];
extern int i;             //客户端编号
extern int listen_lab;
void listen_ans(LPVOID lpParameter);    //监听挑战者的回赢
void run_client(LPVOID lpParameter);    //通过该函数通过线程实现与灭个客户端相连