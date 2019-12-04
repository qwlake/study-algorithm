#include <iostream>
#include <algorithm>
#include <climits>

using namespace std;

int N, M, K;
int a[40], dp[41];

int main() {
	cin >> N;
    cin >> M;
    cin >> K;
    for (int i = 1; i < 41; i++) dp[i] = 0;
	for (int i = 0; i < 40; i++)
        if (i < K)
		    cin >> a[i];
        else
            a[i] = INT_MAX;
    sort(a, a+40);

    dp[1] = 1;
    int m, tmpCnt;
    int nxtHol = a[0];
    int holIdx = 0;
    if (a[0] == 1) {
        nxtHol = a[++holIdx];
        dp[1] = 0;
    }
    for (int i = 2; i <= N; i++) {
        if (nxtHol == i) {
            nxtHol = a[++holIdx];
            continue;
        }
        if (i <= M) {
            dp[i] += 1;
        }
        tmpCnt = 0;
        m = min(i-1, M);
        for (int j = 1; j < m+1; j++) {
            tmpCnt += dp[i-j];
        }
        dp[i] += tmpCnt;
    }

	cout << dp[N] << endl;

	return 0;
}