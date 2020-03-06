#include <stdio.h>

int n, m, arr[101], st[101][2];
int main() {
	scanf("%d", &n);
    for (int i = 1; i <= n; i++) scanf("%d", &arr[i]);
    scanf("%d", &m);
    for (int i = 1; i <= m; i++) scanf("%d %d", &st[i][0], &st[i][1]);
    for (int i = 1; i <= m; i++) {
        if (st[i][0] == 1) {    // man
            for (int j = 1; j <= n/st[i][1]; j++) {
                arr[j*st[i][1]] = !arr[j*st[i][1]];
            }
        } else {                // woman
            arr[st[i][1]] = !arr[st[i][1]];
            for (int j = 1; 0<st[i][1]-j && st[i][1]+j<=n; j++) {
                if (arr[st[i][1]-j] == arr[st[i][1]+j]) {
                    arr[st[i][1]-j] = !arr[st[i][1]-j];
                    arr[st[i][1]+j] = !arr[st[i][1]+j];
                } else break;
            } 
        }
    }
    for (int i = 0; i < (n-1)/21; i++) {
        for (int j = i*20+1; j <= i*20+20; j++) printf("%d ", arr[j]);
        printf("\n");
    }
    int tmp = n/21;
    for (int i = tmp*20+1; i <= (tmp*21)+(n%21); i++) {
        printf("%d ", arr[i]);
    }
	return 0;
}