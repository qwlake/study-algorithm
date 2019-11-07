#include <stdio.h>

int n;
int a[10001];
int sum[10001];

int max(int a, int b) {return a<b?b:a;}

int dp() {
	sum[0] = a[0] + 0;
	sum[1] = sum[0] + a[1];
	for (int i = 2; i < n; i++) {
		sum[i] = max(max(sum[i-2]+a[i], sum[i-3]+a[i-1]+a[i]), sum[i-1]);
	}
	printf("%d", sum[n-1]);
}

int main() {
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%d", &a[i]);
	}
	dp();
	return 0;
}