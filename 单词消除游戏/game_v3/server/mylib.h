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
# define SEARCH_LOG 13                                 //���������־����ͻ���ʵ���������ͳһ
# define BUF_SIZE 50
# define SET_QUE_MAN 2
# define PLAYER 1
# define PROPER_NUM 20
# define MAXNUM_STR 160
# define INC_RANK_RATIO 10               //�ȼ�����ϵ��
# define INC_PLAYER_EXPER_RATIO 10       //�����߾�������ϵ��
# define INC_SETQUE_EXPER_RATIO 20       //�����߾�������ϵ��
# define MAX_CLIENT 40                   //��ͬʱ�������ӵĿͻ��˸�������ͨ���޸ĸ�ֵ�����Ӻͼ��������Ŀͻ���
using namespace std;

extern char all_sendbuf[BUF_SIZE];
extern int i;             //�ͻ��˱��
extern int listen_lab;
void listen_ans(LPVOID lpParameter);    //������ս�ߵĻ�Ӯ
void run_client(LPVOID lpParameter);    //ͨ���ú���ͨ���߳�ʵ��������ͻ�������