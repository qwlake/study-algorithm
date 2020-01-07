#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

int N, ans, cache[501][501], cnt[501][501];
char a[501][501];
string mola = "MOLA";

int dynamic() {
	int k, l;
	for (int i = 1; i < N+1; i++) {
		for (int j = 1; j < N+1; j++) {
			cnt[i][j] = max(cnt[i][j-1], cnt[i-1][j]);
			if (cnt[i][j-1] < cnt[i-1][j]) {
				k = i-1;
				l = j;
			} else if (cnt[i][j-1] > cnt[i-1][j]) {
				k = i;
				l = j-1;
			} else {
				if (cache[i][j-1] < cache[i-1][j]) {
					k = i-1;
					l = j;
				} else {
					k = i;
					l = j-1;
				}
			}
			cnt[i][j] = cnt[k][l];
			if (mola[cache[k][l]] == a[i][j]) {
				if (a[i][j] == 'A') {
					cnt[i][j] += 1;
					cache[i][j] = 0;
				} else {
					cache[i][j] = cache[k][l]+1;
				}
			} else {
				cache[i][j] = 0;
			}
			cout <<  cache[i][j] << " " << cnt[i][j] << "  ";
		}
		cout << endl;
	}
	return cnt[N][N];
}

int main() {
	cin >> N;
	fill_n(a[0], N+1, 'X');
	for (int i = 1; i < N+1; i++) {
		a[i][0] = 'X';
		for (int j = 1; j < N+1; j++) {
			cin >> a[i][j];
			cache[i][j] = 0;
			cnt[i][j] = 0;
		}
	}
	ans = dynamic();
	cout << ans << endl;
	return 0;
}