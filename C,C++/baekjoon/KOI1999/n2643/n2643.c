#include <stdio.h>

int n;
int a[100][2];
int d[100] = {0,};

void insertionSort(int idx) {
	int i;
	int tmp[2] = {a[idx][0], a[idx][1]};
	for (i = idx-1; i >= 0; i--) {
		if (a[i][0] > tmp[0]) {
			a[i+1][0] = a[i][0]; a[i+1][1] = a[i][1];
		} else if (a[i][0] == tmp[0] && a[i][1] > tmp[1]) {
			a[i+1][0] = a[i][0]; a[i+1][1] = a[i][1];
		} else {
			break;
		}
	}
	i++;
	a[i][0] = tmp[0]; a[i][1] = tmp[1];
}

int main() {
	scanf("%d", &n);
	int t1, t2;
	for (int i = 0; i < n; i++) {
		scanf("%d %d", &t1, &t2);
		if (t1 > t2) {
			a[i][0] = t2;
			a[i][1] = t1;
		} else {
			a[i][0] = t1;
			a[i][1] = t2;
		}
		insertionSort(i);
	}
	for (int i = 0; i < n; i++) {
		d[i] = 1;
		for (int j = 0; j < i; j++) {
			if (a[i][1] >= a[j][1]) {
				d[i] = d[i]>d[j]+1? d[i]:d[j]+1;
			}
		}
	}
	for (int i = 1; i < n; i++) {
		d[0] = d[i]>d[0]? d[i]:d[0];
	}
	printf("%d", d[0]);
	return 0;
}