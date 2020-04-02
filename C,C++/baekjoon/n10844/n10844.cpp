#include <iostream>

using namespace std;

int N;
long long a[10][100];

int max(int a, int b) {return a<b?b:a;}

int main() {
	cin >> N;

	for (int i = 0; i < 10; i++)
		a[i][0] = 1;

	long ret = 0;
	for (int i = 1; i < N; i++) {
		for (int j = 1; j < 9; j++) {
			a[j][i] = (a[j-1][i-1] + a[j+1][i-1]) % 1000000000;
		}
		a[0][i] = a[1][i-1] % 1000000000;
		a[9][i] = a[8][i-1] % 1000000000;
	}

	for (int i = 1; i < 10; i++)
		ret += a[i][N-1];
	cout << ret % 1000000000 << endl;

	return 0;
}