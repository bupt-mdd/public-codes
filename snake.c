#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#include<windows.h>
#include<conio.h>
#include<winsock.h>
#include<winbase.h>

#define UP 8
#define DOWN 2
#define LEFT 4
#define RIGHT 6

/*
* 该函数可以实现光标的定位功能。
* 传入参数： x为光标的横坐标；
             y为光标的纵坐标。
*/
void gotoxy(int x, int y)
{
	COORD coord;
	coord.X = x;
	coord.Y = y;
	HANDLE ppy;
	ppy = GetStdHandle(STD_OUTPUT_HANDLE);
	SetConsoleCursorPosition(ppy, coord);
}

//用于存储某一点的横纵坐标值。
struct order {
	int h;
	int z;
};

/*
* 该函数主要用于获取用户输入的方向（UP、DOWN、LEFT、RIGHT）。
*/
void getdirection(void);

/*
* 该函数主要用于实时移动蛇的位置。
*/
void movesnake(void);

char command = '6';					//用于存储玩家的操作命令。
char snake[20][20] = { '\0' };		//数组snake为贪吃蛇游戏的整个活动区域。
int eatnum = 0, snakelength = 0;	//eatnum用于存储吃掉东西的个数，而snakelength用于存储蛇的长度。
struct order snakeorder[400];		//用于存储贪吃蛇身体上每个节点的位置。
main()
{
	int i, j, foodX, foodY;
	char start;
	printf("是否开始游戏？如果是请按回车键：");
	gotoxy(50, 4);
	printf("已经吃到的东西个数：");
	gotoxy(70, 4);
	printf("%d", eatnum);
	gotoxy(50, 8);
	printf("向左----4    向右----6");
	gotoxy(50, 12);
	printf("向上----8    向下----2");
	gotoxy(50, 16);
	printf("暂停----空格键");
	gotoxy(50, 20);
	printf("其它任意键取消暂停");
	gotoxy(0, 1);
	srand(time(NULL));
	//设置贪吃蛇游戏的活动区域
	for (i = 0; i <= 19; i++)
	{
		for (j = 0; j <= 19; j++)
		{
			if (i == 0 || i == 19 || j == 0 || j == 19)
				snake[i][j] = '*';
		}
	}
	//设置贪吃蛇的初始位置和初始长度
	for (i = 10, j = 10; j <= 12; j++)
	{
		snake[i][j] = '@';
		snakeorder[snakelength].h = i;
		snakeorder[snakelength].z = j;
		snakelength++;
	}
	//生成食物节点
	foodX = rand() % 20;
	foodY = rand() % 20;
	while ((snake[foodX][foodY] == '*') || (snake[foodX][foodY] == '@'))
	{
		foodX = rand() % 20;
		foodY = rand() % 20;
	}
	snake[foodX][foodY] = '+';
	//打印显示整个游戏的活动区域和贪吃蛇的初始状态
	for (i = 0; i <= 19; i++)
	{
		for (j = 0; j <= 19; j++)
		{
			printf("%c ", snake[i][j]);
		}
		printf("\n");
	}
	scanf("%c", &start);		//读取开始的命令。
	//线程1主要用于实时获取用户输入的方向信息。并放到全局变量direction中。
	DWORD thread1 = 1;
	HANDLE hthread1 = CreateThread(NULL, 0, (LPTHREAD_START_ROUTINE)getdirection, NULL, 0, &thread1);
	//线程2主要根据direction中的命令信息修改蛇的移动方向，并定期刷新显示蛇的位置。
	DWORD thread2 = 2;
	HANDLE hthread2 = CreateThread(NULL, 0, (LPTHREAD_START_ROUTINE)movesnake, NULL, 0, &thread2);
	while (1)
	{
	}
	system("pause");
	return 0;
}

void getdirection(void)
{
	while (1)
	{
		command = getch();
	}
}

void movesnake(void)
{
	int i;
	int j;
	int foodX;					//存放食物的横坐标。
	int foodY;					//存放食物的纵坐标。
	int headX;					//存放蛇头节点的横坐标。
	int headY;					//存放蛇头节点的纵坐标。
	int rearX;					//存放蛇尾节点的横坐标。
	int rearY;					//存放蛇尾节点的纵坐标。
	int temprearX;				//存放蛇尾（每次刷新前的蛇尾节点）节点的横坐标。
	int temprearY;				//存放蛇尾（每次刷新前的蛇尾节点）节点的纵坐标。
	int intcommand = RIGHT;		//存放用户输入的命令。
	int direction = RIGHT;		//存放纠正后的方向信息。

	temprearX = 10;
	temprearY = 10;
	rearX = snakeorder[snakelength - 1].h;
	rearY = snakeorder[snakelength - 1].z;
	while (1 && ((snake[rearX][rearY] != '*') && (snake[rearX][rearY] != '@')) || prime == 1)
	{
		if (command == ' ')
			Sleep(300);
		else
		{
			intcommand = command - 48 ;
			//方向纠错
			if ((direction == RIGHT && intcommand == LEFT) ||
				(intcommand == UP && direction == DOWN) ||
				(direction == LEFT && intcommand == RIGHT) ||
				(intcommand == DOWN && direction == UP) ||
				(intcommand != LEFT && intcommand != DOWN && intcommand != RIGHT && intcommand != UP))
				intcommand = direction;
			else
				direction = intcommand;	 
			
			//吃入食物时
			if (snake[rearX][rearY] == '+') 
			{
				snake[rearX][rearY] = '@';
				gotoxy(2 * rearY, rearX + 1);
				printf("@");
				gotoxy(70, 4);
				printf("%d", ++eatnum);
				for (i = snakelength; i>0; i--)
				{
					snakeorder[i] = snakeorder[i - 1];
				}
				headX = temprearX;
				headY = temprearY;
				snakeorder[i].h = headX;
				snakeorder[i].z = headY;
				snake[headX][headY] = '@';
				snakelength++;
				//随机生成一个活动节点。
				foodX = rand() % 20;
				foodY = rand() % 20;
				while ((snake[foodX][foodY] == '*') || (snake[foodX][foodY] == '@'))
				{
					foodX = rand() % 20;
					foodY = rand() % 20;
				}
				snake[foodX][foodY] = '+';
				gotoxy(2 * foodY, foodX + 1);
				printf("%c", snake[foodX][foodY]);
			}
			else if (snake[rearX][rearY] == '*') {	//游戏失败。
				return;
			}
			else
			{	//移动蛇的身体。
				snake[rearX][rearY] = '@';
				gotoxy(2 * rearY, rearX + 1);
				printf("@");
				gotoxy(2 * temprearY, temprearX + 1);
				printf(" ");
			}
			switch (direction)
			{
			case UP:
				headX = snakeorder[0].h;
				headY = snakeorder[0].z;
				rearX = rearX - 1;
				snakeorder[snakelength].h = rearX;
				snakeorder[snakelength].z = rearY;
				snake[headX][headY] = '\0';
				temprearX = headX;
				temprearY = headY;
				for (i = 0; i<snakelength; i++)
				{
					snakeorder[i] = snakeorder[i + 1];
				}
				break;
			case DOWN:
				headX = snakeorder[0].h;
				headY = snakeorder[0].z;
				rearX = rearX + 1;
				snakeorder[snakelength].h = rearX;
				snakeorder[snakelength].z = rearY;
				snake[headX][headY] = '\0';
				temprearX = headX;
				temprearY = headY;
				for (i = 0; i<snakelength; i++)
				{
					snakeorder[i] = snakeorder[i + 1];
				}
				break;
			case LEFT:
				headX = snakeorder[0].h;
				headY = snakeorder[0].z;
				rearY = rearY - 1;
				snakeorder[snakelength].h = rearX;
				snakeorder[snakelength].z = rearY;
				snake[headX][headY] = '\0';
				temprearX = headX;
				temprearY = headY;
				for (i = 0; i<snakelength; i++)
				{
					snakeorder[i] = snakeorder[i + 1];
				}
				break;
			case RIGHT:
				headX = snakeorder[0].h;
				headY = snakeorder[0].z;
				rearY = rearY + 1;
				snakeorder[snakelength].h = rearX;
				snakeorder[snakelength].z = rearY;
				snake[headX][headY] = '\0';
				temprearX = headX;
				temprearY = headY;
				for (i = 0; i<snakelength; i++)
				{
					snakeorder[i] = snakeorder[i + 1];
				}
				break;
			}
			Sleep(300);
		}
	}
}
