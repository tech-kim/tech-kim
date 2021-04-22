#include <stdio.h>
#include <time.h>


void initData();

int level;
int arrayFish[6];

int* cursor;

void printfFishes();
void decreaseWater(long elapsedTime);


int main(void)
{
	long startTime = 0;
	long totalElapsedTime = 0;
	long prevElapsedTime = 0;

	int num;
	initData();

	cursor = arrayFish;
	startTime = clock();
	while (1)
	{
		printfFishes();
		printf("몇 번 어항에 물을 주시겠어요?");
		scanf_s("%d", &num);

		if (num < 1 || num>6)
		{
			printf("\n입력값이 잘못되었습니다\n");
			continue;
		}
		
		totalElapsedTime = (clock() - startTime) / CLOCKS_PER_SEC;
		printf("총 경과 시간 : %ld 초\n", totalElapsedTime);

		prevElapsedTime = totalElapsedTime - prevElapsedTime;
		printf("최근 경과 시간 : %ld 초\n", prevElapsedTime);

		decreaseWater(prevElapsedTime);

		if (cursor[num - 1] <= 0)
		{
			printf("%d 번 물고기는 이미 죽었습니다. ㅠㅠ\n", num);
		}
		else if (cursor[num - 1] + 1 <= 100)
		{
			printf(" %d 번 어항에 물을 줍니다\n\n", num);
			cursor[num - 1] += 1;
		}

		if (totalElapsedTime / 20 > level - 1)
		{
			level++;
			printf("*** 축! 레벨업! 기존 %d 레벨에서 %d 레벨로 업그레이드 ***", level - 1, level);

			if (level == 5)
			{
				printf("\n\n축하합니다. 최고 레벨을 달성하였습니다. 게임을 종료합니다.");
				exit(0);
			}
		}
		if (checkFishAlive() == 0)
		{
			printf("모든 물고기가 죽었습니다...\n");
			exit(0);
		}
		else
		{
			printf("아직 물고기가 살아있어요\n");
		}
		prevElapsedTime = totalElapsedTime;
	}
	return 0;
}

void initData()
{
	level = 1;
	for (int i = 0; i < 6; i++)
	{
		arrayFish[i] = 100;
	}
}

void printfFishes()
{
	printf("%3d번 %3d번 %3d번 %3d번 %3d번 %3d번\n", 1, 2, 3, 4, 5, 6);
	for (int i = 0; i < 6; i++)
	{
		printf(" %4d ", arrayFish[i]);
	}
	printf("\n\n");
}

void decreaseWater(long elapsedTime)
{
	for (int i = 0; i < 6; i++)
	{
		arrayFish[i] -= (level * 3 * (int)elapsedTime);
		if (arrayFish[i] < 0)
		{
			arrayFish[i] = 0;
		}
	}
}

int checkFishAlive()
{
	for (int i = 0; i < 6; i++)
	{
		if (arrayFish[i] > 0)
			return 1;
	}
	return 0;
}
