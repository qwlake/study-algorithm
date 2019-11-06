#include <stdio.h>

int max(int a, int b) {return a<b?b:a;}

int loop(int *a, int size, int idx, int cups, int sum) {
	int x = 0; int y = 0;
	if (idx < size) {
		if (cups == 0) {
			x = loop(a, size, idx+1, 1, sum+a[idx]);
		} else  {
			x = loop(a, size, idx+1, 0, sum);
		}	
		if (cups == 1) {
			y = loop(a, size, idx+1, 2, sum+a[idx]);
		}
		
		return max(x,y);
	} else return sum;
}

int main() {
    int n;
	scanf("%d", &n);
	int a[10000];
	for (int i = 0; i < n; i++) {
		scanf("%d", &a[i]);
	}
	int ret = loop(a, n, 0, 0, 0);
	printf("%d", ret);
	return 0;
}