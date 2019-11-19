#include <iostream>
using namespace std;

int N, ans, dp[19];
char a[19];

int get(char o, int a, int b) {
	if (o == '-') return a-b;
	else if (o == '+') return a+b;
	else return a*b;
}

// It's not passed with this code! Try again with Python.
int main() {
	cin >> N;
	for (int i = 0; i < N; i++) {
		cin >> a[i];
	}

	dp[0] = a[0]-'0';
	if (N >= 3) {
		dp[2] = get(a[1], a[0]-'0', a[2]-'0');
	}
	int tmp1, tmp2;
	for (int i = 4; i < N; i=i+2) {
		tmp1 = get(a[i-1], dp[i-2], a[i]-'0'); // 2번 전과 1번 전 원소를 괄호로 
		tmp2 = get(a[i-3], dp[i-4], get(a[i-1], a[i-2]-'0', a[i]-'0')); // 1번 전과 현재 원소를 괄호로
		if (i < N-4 && a[i-1]=='-' && a[i+1]=='*' && a[i+3]=='-') // 음수 곱하기 음수인 경우
			dp[i] = tmp2;
		else
			dp[i] = tmp1<tmp2? tmp2:tmp1;
	}

	cout << dp[N-1] << endl;

	return 0;
}