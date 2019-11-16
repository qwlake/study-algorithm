#include <iostream>
#include <algorithm>

using namespace std;

int N, a[1001], d[1001], ans;

int main() {
	cin >> N;
	for (int i = 1; i < N+1; i++)
		cin >> a[i];

	for (int i = 1; i <= N; i++) {
		d[i] = 1;
		for (int j = 1; j <= i; j++) {
			if (a[i] > a[j]) {
				d[i] = max(d[i], d[j]+1);
			}
		}
	}

	for (int i = 1; i <= N; i++) {
		ans = d[i]<ans? ans:d[i];
	}

	cout << ans << endl;

	return 0;
}