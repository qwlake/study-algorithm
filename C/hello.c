#include <stdio.h>
#include <stdlib.h>

int main() {
    int n = 0;
	scanf("%d", &n);
	int arr[1000][3];
	for (int i = 0; i < n; i++) {
		scanf("%d %d %d", &arr[i][0], &arr[i][1], &arr[i][2]);
	}

    

	for (int i = 0; i < n; i++) {
		printf("%d %d %d", arr[i][0], arr[i][1], arr[i][2]);
	}
	return 0;
}