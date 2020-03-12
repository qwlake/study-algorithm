#include <stdio.h>

int n, m=0;
int ans[100], arr[100];

void loop(int p, int q, int k) {
    if (p < 0) {
        if (m < k) {
            m = k;
            for (int i = 0; i < k; i++) {
                ans[i] = arr[i];
            }
        }
        return;
    }
    arr[k] = q;
    loop(q, p-q, k+1);
}

int main() {
	scanf("%d", &n);
    if (n == 1) {
        printf("4\n1 1 0 1");
        return 0;
    }
    int i, stNum, edNum;
    stNum = (n/2)+(n%2);
    edNum = n-(stNum/2)+(stNum%2);
    for (i = stNum; i < edNum; i++) {
        loop(n, i, 0);
    }
    printf("%d\n%d ", m, n);
    for (i = 0; i < m-1; i++) {
        printf("%d ", ans[i]);
    }
	return 0;
}