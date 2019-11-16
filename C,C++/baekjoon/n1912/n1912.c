#include <stdio.h>

int n;
int a[100001];

int max(int a, int b) {return a<b?b:a;}

int main() {
	scanf("%d", &n);
	for (int i = 0; i < n; i++)
		scanf("%d", &a[i]);

	int max = a[0] + 0;
	int sum = a[0] + 0;
	int temp = 0;
	for (int i = 1; i < n; i++) {
		temp = sum+a[i];
		if (temp > 0)
			sum += a[i];
		if (max<sum)
			max = sum;
		if (temp <= 0)
			sum = 0;
	}
	if (max == 0) {
		max = a[0] + 0;
		for (int i = 0; i < n; i++)
			max = max<a[i]? a[i]:max;
	}
	printf("%d",max);

	return 0;
}