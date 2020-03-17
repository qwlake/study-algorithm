#include <stdio.h>

int row, col, n, a[100], b[100], tmp;
int as = 0;
int bs = 0;

void swap(int *x, int *y) {
    tmp = *x;
    *x = *y;
    *y = tmp;
}

void sort(int arr[], int size) {
    for (int i = 1; i < size; i++) {
        for (int j = i; j > 0; j--) {
            if (arr[j-1] > arr[j]) swap(&arr[j-1], &arr[j]);
            else break;
        }
    }
}

int main() {
	scanf("%d %d\n%d", &col, &row, &n);
    a[as++] = 0; b[bs++] = 0;
    for (int i = 0; i < n; i++) {
        scanf("%d", &tmp);
        if (tmp == 0) scanf("%d", &a[as++]); 
        else scanf("%d", &b[bs++]); 
    }
    a[as++] = row; b[bs++] = col;
    sort(a, as); sort(b, bs);
    int max = 0;
    for (int i = 0; i < as-1; i++) {
        for (int j = 0; j < bs-1; j++) {
            tmp = (a[i+1]-a[i])*(b[j+1]-b[j]);
            max = max<tmp?tmp:max;
        }
    }
    printf("%d", max);
	return 0;
}