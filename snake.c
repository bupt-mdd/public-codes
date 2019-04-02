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
* �ú�������ʵ�ֹ��Ķ�λ���ܡ�
* ��������� xΪ���ĺ����ꣻ
             yΪ���������ꡣ
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

//���ڴ洢ĳһ��ĺ�������ֵ��
struct order {
	int h;
	int z;
};

/*
* �ú�����Ҫ���ڻ�ȡ�û�����ķ���UP��DOWN��LEFT��RIGHT����
*/
void getdirection(void);

/*
* �ú�����Ҫ����ʵʱ�ƶ��ߵ�λ�á�
*/
void movesnake(void);

char command = '6';					//���ڴ洢��ҵĲ������
char snake[20][20] = { '\0' };		//����snakeΪ̰������Ϸ�����������
int eatnum = 0, snakelength = 0;	//eatnum���ڴ洢�Ե������ĸ�������snakelength���ڴ洢�ߵĳ��ȡ�
struct order snakeorder[400];		//���ڴ洢̰����������ÿ���ڵ��λ�á�
main()
{
	int i, j, foodX, foodY;
	char start;
	printf("�Ƿ�ʼ��Ϸ��������밴�س�����");
	gotoxy(50, 4);
	printf("�Ѿ��Ե��Ķ���������");
	gotoxy(70, 4);
	printf("%d", eatnum);
	gotoxy(50, 8);
	printf("����----4    ����----6");
	gotoxy(50, 12);
	printf("����----8    ����----2");
	gotoxy(50, 16);
	printf("��ͣ----�ո��");
	gotoxy(50, 20);
	printf("���������ȡ����ͣ");
	gotoxy(0, 1);
	srand(time(NULL));
	//����̰������Ϸ�Ļ����
	for (i = 0; i <= 19; i++)
	{
		for (j = 0; j <= 19; j++)
		{
			if (i == 0 || i == 19 || j == 0 || j == 19)
				snake[i][j] = '*';
		}
	}
	//����̰���ߵĳ�ʼλ�úͳ�ʼ����
	for (i = 10, j = 10; j <= 12; j++)
	{
		snake[i][j] = '@';
		snakeorder[snakelength].h = i;
		snakeorder[snakelength].z = j;
		snakelength++;
	}
	//����ʳ��ڵ�
	foodX = rand() % 20;
	foodY = rand() % 20;
	while ((snake[foodX][foodY] == '*') || (snake[foodX][foodY] == '@'))
	{
		foodX = rand() % 20;
		foodY = rand() % 20;
	}
	snake[foodX][foodY] = '+';
	//��ӡ��ʾ������Ϸ�Ļ�����̰���ߵĳ�ʼ״̬
	for (i = 0; i <= 19; i++)
	{
		for (j = 0; j <= 19; j++)
		{
			printf("%c ", snake[i][j]);
		}
		printf("\n");
	}
	scanf("%c", &start);		//��ȡ��ʼ�����
	//�߳�1��Ҫ����ʵʱ��ȡ�û�����ķ�����Ϣ�����ŵ�ȫ�ֱ���direction�С�
	DWORD thread1 = 1;
	HANDLE hthread1 = CreateThread(NULL, 0, (LPTHREAD_START_ROUTINE)getdirection, NULL, 0, &thread1);
	//�߳�2��Ҫ����direction�е�������Ϣ�޸��ߵ��ƶ����򣬲�����ˢ����ʾ�ߵ�λ�á�
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
	int foodX;					//���ʳ��ĺ����ꡣ
	int foodY;					//���ʳ��������ꡣ
	int headX;					//�����ͷ�ڵ�ĺ����ꡣ
	int headY;					//�����ͷ�ڵ�������ꡣ
	int rearX;					//�����β�ڵ�ĺ����ꡣ
	int rearY;					//�����β�ڵ�������ꡣ
	int temprearX;				//�����β��ÿ��ˢ��ǰ����β�ڵ㣩�ڵ�ĺ����ꡣ
	int temprearY;				//�����β��ÿ��ˢ��ǰ����β�ڵ㣩�ڵ�������ꡣ
	int intcommand = RIGHT;		//����û���������
	int direction = RIGHT;		//��ž�����ķ�����Ϣ��

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
			//�������
			if ((direction == RIGHT && intcommand == LEFT) ||
				(intcommand == UP && direction == DOWN) ||
				(direction == LEFT && intcommand == RIGHT) ||
				(intcommand == DOWN && direction == UP) ||
				(intcommand != LEFT && intcommand != DOWN && intcommand != RIGHT && intcommand != UP))
				intcommand = direction;
			else
				direction = intcommand;	 
			
			//����ʳ��ʱ
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
				//�������һ����ڵ㡣
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
			else if (snake[rearX][rearY] == '*') {	//��Ϸʧ�ܡ�
				return;
			}
			else
			{	//�ƶ��ߵ����塣
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
