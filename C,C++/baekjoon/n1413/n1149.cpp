#include <iostream>
#include <algorithm>

using namespace std;

int N, M, a[20][20], ans1, ans2;

void loop(int r, int c) {
	
	if (c+1 < N) {
		
		if (r+1 < M) loop(r+1, c+1);
		else ans2++;
		for (int i = 0; i < c+1; i++) loop(r, c+1);
	} else {
		ans1++;
	}
}

int main() {
	cin >> N;
	cin >> M;
	// for (int i = 1; i < N+1; i++)
	// 	cin >> a[i];

	for (int i = 0; i < M; i++) {
		for (int j = 0; j < N; j++) {
			a[i][j] = 0;
		}
	}

	loop(0, 0);
	// ans2 += ans1;
	int div = ans1;
	// while (true) {
	// 	if (ans1%div == 0 && ans2%div == 0) {
	// 		ans1 /= div;
	// 		ans2 /= div;
	// 		break;
	// 	} else {
	// 		div--;
	// 	}
	// }

	cout << ans1 << "/" << ans2 << endl;

	return 0;
}


// #include "stdio.h"

// typedef long long ll;
// int n, m;
// ll dp[21][21] = { 0, }, div;
// ll gcd(ll a, ll b) {
// 	return b ? gcd(b, a%b) : a;
// }

// ll solve(int n, int k) {
// 	if (n == 0) return 1;
// 	if (k == 0) return 0;

// 	ll & ret = dp[n][k];
// 	if (ret != 0) return ret;

// 	return ret = solve(n - 1, k - 1) + (n - 1)*solve(n - 1, k);
// }

// int main() {
// 	scanf("%d %d", &n, &m);
// 	div = gcd(solve(n, n), solve(n, m));

// 	printf("%lld/%lld", solve(n, m), solve(n, n));

// 	return 0;
// }