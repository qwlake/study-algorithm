#include <iostream>
#include <algorithm>
using namespace std;

int N, ans, dp[500][500];
char a[500][500];

int loop(int r, int c, int total, int cnt) {
	int tmp[2] = {0,0};
	if (a[r][c] == 'M') {
		if (r+1 < N) tmp[0] = loop(r+1, c, total, 1);
		if (c+1 < N) tmp[1] = loop(r, c+1, total, 1);
	} else if (cnt == 1 && a[r][c] == 'O') {
		if (r+1 < N) tmp[0] = loop(r+1, c, total, cnt+1);
		if (c+1 < N) tmp[1] = loop(r, c+1, total, cnt+1);
	} else if (cnt == 2 && a[r][c] == 'L') {
		if (r+1 < N) tmp[0] = loop(r+1, c, total, cnt+1);
		if (c+1 < N) tmp[1] = loop(r, c+1, total, cnt+1);
	} else if (cnt == 3 && a[r][c] == 'A') {
		if (r+1 < N) tmp[0] = loop(r+1, c, total+1, 0);
		if (c+1 < N) tmp[1] = loop(r, c+1, total+1, 0);
	} else {
		if (r+1 < N) tmp[0] = loop(r+1, c, total, 0);
		if (c+1 < N) tmp[1] = loop(r, c+1, total, 0);
	}
	return max(max(tmp[0], tmp[1]), total);
}

int dynamic() {
	return 0;
}

int main() {
	cin >> N;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cin >> a[i][j];
		}
	}
	ans = loop(0, 0, 0, 0);
	cout << ans << endl;
	return 0;
}