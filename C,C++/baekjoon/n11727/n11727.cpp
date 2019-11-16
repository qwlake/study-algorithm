#include <iostream>

using namespace std;

int N;
long long a[1001];

int max(int a, int b) {return a<b?b:a;}

int main() {
	cin >> N;
	// for (int i = 0; i < N; i++)
	// 	cin >> a[i];

	a[1] = 1;
	a[2] = 3;
	a[3] = 5;

	for (int i = 4; i <= N; i++) {
		a[i] = (a[i-1] + a[i-2]*2)%10007;
	}

	cout << a[N];

	return 0;
}