#include <stdio.h>
#include <limits.h>

int main() {
    int n = 0;
	scanf("%d", &n);
	int a[1000][3];
	int b[1000][3];
	for (int i = 0; i < n; i++) {
		scanf("%d %d %d", &a[i][0], &a[i][1], &a[i][2]);
	}

	int temp1, temp2;
    for (int i = 1; i < n; i++) {
		temp1 = a[i][0] + a[i-1][1];
		temp2 = a[i][0] + a[i-1][2];
		a[i][0] = (temp1<temp2)? temp1:temp2;
		temp1 = a[i][1] + a[i-1][0];
		temp2 = a[i][1] + a[i-1][2];
		a[i][1] = (temp1<temp2)? temp1:temp2;
		temp1 = a[i][2] + a[i-1][0];
		temp2 = a[i][2] + a[i-1][1];
		a[i][2] = (temp1<temp2)? temp1:temp2;
	}

	int min = INT_MAX;
	for (int i = 0; i < 3; i++) {
		min = (a[n-1][i] < min)? a[n-1][i]:min;
	}
	printf("%d", min);
	return 0;
}