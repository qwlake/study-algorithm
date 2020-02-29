#include <stdio.h>

int a[8][8] = {0,};
int d[4][2] = {{-1, 0}, 	// up
			   {0, 1}, 		// right
			   {1, 0}, 		// down
			   {0, -1}};	// left
int opp[7] = {0,};

void findOpposite(int path[7], int direction, int cnt, int x, int y, int n) {
	int target;
	for (int i = 0; i < 4; i++) {
		target = a[x+d[i][0]][y+d[i][1]];
		if (x+d[i][0] > 0 && y+d[i][1] > 0 && 
			x+d[i][0] < 8 && y+d[i][1] < 8 &&
			target != 0 && 
			path[target] == 0) {
			path[target] = 1;
			if (direction == -1) {
				findOpposite(path, i, 1, x+d[i][0], y+d[i][1], n);
			} else if (direction==i && cnt==1 &&
					   (opp[n]==0 || opp[n]==target) &&
					   (opp[target]==0 || opp[target]==n)) {
				opp[n] = target;
				opp[target] = n;
				findOpposite(path, direction, cnt+1, x+d[i][0], y+d[i][1], n);
			} else {
				findOpposite(path, direction, cnt, x+d[i][0], y+d[i][1], n);
			}
		}
	}
}

int main() {
	for (int i = 1; i < 7; i++) {
		for (int j = 1; j < 7; j++) {
			scanf("%d", &a[i][j]);
		}
	}
	for (int i = 1; i < 7; i++) {
		for (int j = 1; j < 7; j++) {
			if (a[i][j] != 0) {
				int path[7] = {0,};
				path[a[i][j]] = 1;
				findOpposite(path, -1, 0, i, j, a[i][j]);
			}
		}
	}
	int flag = 0;
	for (int i = 1; i < 7; i++) {
		if (opp[i] == 0) flag = 1;
	}
	if (flag) printf("%d",0);
	else printf("%d", opp[1]);
	return 0;
}