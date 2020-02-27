#include <iostream>
#include <climits>
#include <string.h>

using namespace std;

int N, M;
char *a1, *a2, *a1Ans, *a2Ans;
int **dp;

char *dataInput(int *length) {
	cin >> *length;
    char *a;
    a = new char[*length];
    for (int i = 0; i < *length; i++)
        cin >> a[i];
    return a;
}

int max(int a, int b, int c=INT_MIN) {
    int tmp = a>b?a:b;
    return tmp>c?tmp:c;
}

int main() {
    a1 = dataInput(&N); a2 = dataInput(&M);
    dp = new int*[N];
    for (int i = 0; i < N; i++) {
        dp[i] = new int[M]();
    }

    for (int i = 0; i < M; i++) {
        if (a1[0] == a2[i]) {
            dp[0][i] = 3;
        } else {
            dp[0][i] = -2;
        }
    }
    int tmp;
    for (int i = 1; i < N; i++) {
        dp[i-1][0] = (dp[i-1][0] < 0)? 0:dp[i-1][0];
        if (a1[i] == a2[0]) {
            dp[i][0] = dp[i-1][0]+3;
        } else {
            dp[i][0] = dp[i-1][0]-2;
        }
        for (int j = 1; j < M; j++) {
            tmp = max(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]);
            if (a1[i] == a2[j]) {
                dp[i][j] = tmp+3;
            } else {
                dp[i][j] = tmp-2;
            }
        }
    }
    
    int m=0, x=0, y=0;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++)
            if (dp[i][j]>m) {
                m = dp[i][j];
                x = i; y = j;
            }
    }
    
    a1Ans = new char[1000]; a2Ans = new char[1000];
    int a1AnsLen = 1, a2AnsLen = 1;
    a1Ans[0] = a1[x]; a2Ans[0] = a2[y];
    int failCnt = 0;
    while (failCnt < 2) {
        if (x-1 >= 0 && dp[x-1][y] > 0) {
            x--;
            a1Ans[a1AnsLen++] = a1[x];
            failCnt = 0;
        } else failCnt++;
        if (y-1 >= 0 && dp[x][y-1] > 0) {
            y--;
            a2Ans[a2AnsLen++] = a2[y];
            failCnt = 0;
        } else failCnt++;
    }

    cout << m << endl;
    for (int i = a1AnsLen-1; i >= 0; i--)
        cout << a1Ans[i];
    cout << endl;
    for (int i = a2AnsLen-1; i >= 0; i--)
        cout << a2Ans[i];
		
	return 0;
}