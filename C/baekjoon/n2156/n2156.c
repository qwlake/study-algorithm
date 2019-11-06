#include <stdio.h>

int max(int a, int b) {return a<b?b:a;}

int possible(int *isDrinked, int idx) {
	int t1 = isDrinked[idx-1] + isDrinked[idx-2];
	int t2 = isDrinked[idx+1] + isDrinked[idx+2];
	if (t1 == 2 || t1 == 2) return 0;
	else return 1;
}

int main() {
    int n;
	scanf("%d", &n);
	int a[10000];
	int sum[10000] = {0};
	int isDrinked[10000] = {0};
	for (int i = 0; i < n; i++) {
		scanf("%d", &a[i]);
	}

	sum[0] = a[0]+0;
	if (n > 1) sum[1] = sum[0] + a[1];
	if (n > 2) {
		int x = sum[1]-a[1]+a[2];
		int y = sum[1]-a[0]+a[2];
		int m = max(max(sum[1], x), y);
		if (m == x) {
			isDrinked[0] = 1;
			isDrinked[2] = 1;
		} else if (m == y) {
			isDrinked[1] = 1;
			isDrinked[2] = 1;
		}
		sum[2] = m;
	}

	int x,y,z,m,t;
	for (int i = 3; i < n; i++) {
		t = isDrinked[i-2];
		isDrinked[i-2] = 0;
		x = possible(isDrinked, i-3)? sum[i-1]-a[i-2]+a[i]+a[i-3]:0;
		isDrinked[i-2] = t;
		y = sum[i-1]-a[i-3]+a[i];
		m = max(max(sum[i-1], y), x);
		if (m == x) {
			isDrinked[i-2] = 0;
			isDrinked[i] = 1;
			isDrinked[i-3] = 1;
		} else if (m == y) {
			isDrinked[i-3] = 0;
			isDrinked[i] = 1;
		}
		sum[i] = m;
	}
	printf("%d", sum[n-1]);
	return 0;
}