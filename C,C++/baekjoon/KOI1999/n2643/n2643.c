#include <stdio.h>

int n;
int a[100][2] = {0,};
int used[100] = {0,};

int dfs(int pre, int cnt) {
	int ret[100] = {1,};
	int max = cnt;
	for (int i = 0; i < n; i++) {
		if (used[i] == 0 && 
			((a[pre][0] >= a[i][0] &&
			a[pre][1] >= a[i][1]) ||
			(a[pre][0] >= a[i][1] &&
			a[pre][1] >= a[i][0]))) {
			used[i] = 1;
			ret[i] = dfs(i, cnt+1);
			used[i] = 0;
		}
	}
	for (int i = 0; i < n; i++) {
		max = max<ret[i]?ret[i]:max;
	}
	return max;
}

int main() {
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < 2; j++) {
			scanf("%d", &a[i][j]);
		}
	}




	// int ret[100] = {1,};
	// int max = 0;
	// for (int i = 0; i < n; i++) {
	// 	used[i] = 1;
	// 	ret[i] = dfs(i, 1);
	// 	used[i] = 0;
	// }
	// for (int i = 0; i < n; i++) {
	// 	max = max<ret[i]?ret[i]:max;
	// }
	// printf("%d", max);
	return 0;
}