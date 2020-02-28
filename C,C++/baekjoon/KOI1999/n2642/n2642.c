#include <stdio.h>

int a[8][8] = 0;
int dir[4][2] = {{-1, 0}, 	// up
				 {0, 1}, 	// right
				 {1, 0}, 	// down
				 {0, -1}};	// left
int square[3][3] = 0;
int set[7] = 0;

int main() {
	for (int i = 1; i < 7; i++) {
		for (int j = 1; j < 7; j++) {
			scanf("%d", &a[i][j]);
		}
	}

	int posX, posY;
	for (int i = 0; i < 6; i++) { 	// 1 위치
		for (int j = 0; j < 6; j++) {
			printf("%d ", a[i][j]);
			if (a[i][j] == 1) {
				posX,posY = i,j;
				set[1] = 1;
			}
		}
		printf("\n");
	}

	for (int i = 0; i < 4; i++) { 	// 1 주변 4방향 관리
		if (a[posX+dir[i][0]][posY+dir[i][1]] != 0) {
			if (square[dir[i][0]+1][dir[i][1]+1] != 0) return;
			square[dir[i][0]+1][dir[i][1]+1] = a[posX+dir[i][0]][posY+dir[i][1]];
			set[a[posX+dir[i][0]][posY+dir[i][1]]] = 1;
		}
	}

	return 0;
}