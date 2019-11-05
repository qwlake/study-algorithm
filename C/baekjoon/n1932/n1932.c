#include <stdio.h>

int max(int a, int b) {return a<b?b:a;}

int main() {
    int n;
	scanf("%d", &n);
	
	int a[500][500];
	for (int i = 0; i < n; i++)
		for (int j = 0; j <= i; j++)
			scanf("%d", &a[i][j]);

	for (int i = 1; i < n; i++) {
		a[i][0] = a[i][0] + a[i-1][0];
		for (int j = 1; j <= i+1; j++) {
			a[i][j] = max(a[i][j]+a[i-1][j], a[i][j]+a[i-1][j-1]);
		}
	}

	int max = 0;
	for (int i = 0; i < n; i++) {
		max = max < a[n-1][i]? a[n-1][i]:max;
	}
	printf("%d", max);
}