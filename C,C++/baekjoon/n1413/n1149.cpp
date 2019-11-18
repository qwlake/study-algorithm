#include <iostream>
using namespace std;

typedef long long ll;

int N, M;
ll ans1, ans2, d;

ll gcd(ll a, ll b){ return b ? gcd(b, a%b) : a; }

ll loop(int m, int n) {
	if (n == 0) return 1;
	if (m == 0) return 0;
	return (n-1)*loop(m, n-1) + loop(m-1, n-1);
}

int main() {
	cin >> N;
	cin >> M;
	// for (int i = 1; i < N+1; i++)
	// 	cin >> a[i];

	ans1 = loop(M, N);
	ans2 = 1;
	for (int i = 2; i < N+1; i++)
		ans2 *= i;
	d = gcd(ans1, ans2);

	cout << ans1/d << "/" << ans2/d << endl;

	return 0;
}