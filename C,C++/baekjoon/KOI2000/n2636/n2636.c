#include <stdio.h>

int row, col, tmp, a[102][102]={0};

int loop(int x, int y, int notPassed) {
    if (0<=y-1)
        if (a[x][y-1]==notPassed) {a[x][y-1]--; loop(x, y-1, notPassed);}
        else if (a[x][y-1]==1) a[x][y-1]=2;
    if (x+1<row)
        if (a[x+1][y]==notPassed) {a[x+1][y]--; loop(x+1, y, notPassed);}
        else if (a[x+1][y]==1) a[x+1][y]=2;
    if (y+1<col)
        if (a[x][y+1]==notPassed) {a[x][y+1]--; loop(x, y+1, notPassed);}
        else if (a[x][y+1]==1) a[x][y+1]=2;
    if (0<=x-1)
        if (a[x-1][y]==notPassed) {a[x-1][y]--; loop(x-1, y, notPassed);}
        else if (a[x-1][y]==1) a[x-1][y]=2;
}
int check(int arg) {
    tmp = 0;
    for (int i = 0; i < row; i++) {
        for (int j = 0; j < col; j++) {
            if (a[i][j] == 2) {
                a[i][j] = arg;
                tmp++;
            } else if (a[i][j] == 0) {
                a[i][j] = arg;
            }
        }
    }
    return tmp;
}

int main() {
	scanf("%d %d", &row, &col);
    row += 2;
    col += 2;
    for (int i = 1; i < row-1; i++) {
        for (int j = 1; j < col-1; j++) {
            scanf("%d", &a[i][j]);
        }
    }
    int arg = 0;
    int cheese = 0;
    int ret = 0;
    while (1) {
        loop(0, 0, arg);
        cheese = check(arg-1);
        arg--;
        if (cheese != 0) ret = cheese;
        else break;
    }
    printf("%d\n%d", -(arg+1), ret);
	return 0;
}