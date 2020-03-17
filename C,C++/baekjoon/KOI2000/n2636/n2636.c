#include <stdio.h>

int row, col, tmp, a[100][100];

int loop(int x, int y) {
    if (0<=y-1)
        if (a[x][y-1]==0) {a[x][y-1]--; loop(x, y-1);}
        else if (a[x][y-1]==1) a[x][y-1]=2;
    if (x+1<row)
        if (a[x+1][y]==0) {a[x+1][y]--; loop(x+1, y);}
        else if (a[x+1][y]==1) a[x+1][y]=2;
    if (y+1<col)
        if (a[x][y+1]==0) {a[x][y+1]--; loop(x, y+1);}
        else if (a[x][y+1]==1) a[x][y+1]=2;
    if (0<=x-1)
        if (a[x-1][y]==0) {a[x-1][y]--; loop(x-1, y);}
        else if (a[x-1][y]==1) a[x-1][y]=2;
}
int check() {
    tmp = 0;
    for (int i = 0; i < row; i++) {
        for (int j = 0; j < col; j++) {
            if (a[i][j] == 2) {
                a[i][j] = 0;
                tmp++;
            } else if (a[i][j] == -1) {
                a[i][j] = 0;
            }
        }
    }
    return tmp;
}

int main() {
	scanf("%d %d", &row, &col);
    for (int i = 0; i < row; i++) {
        for (int j = 0; j < col; j++) {
            scanf("%d", &a[i][j]);
        }
    }
    int n = 0;
    int cheese = 0;
    int ret = 0;
    while (1) {
        loop(0, 0);
        cheese = check();
        n++;
        if (cheese != 0) ret = cheese;
        else break;
    }
    printf("%d\n%d", n-1, ret);
	return 0;
}