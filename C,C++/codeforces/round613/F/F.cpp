#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

int N, tmp, ans, a[100000];

int gcd(int a, int b){
	while(b!=0){
		int r = a%b;
		cout << r << endl;
		a= b;
		b= r;
	}
	return a;
}

int lcm(int a, int b){
    return a * b / gcd(a,b);
}

int main() {
	cin >> N;
	for (int i = 0; i < N; i++) {
		cin >> a[i];
	}
	ans = 0;
	for (int i = 0; i < N-1; i++) {
		for (int j = i+1; j < N; j++) {
			tmp = lcm(a[i],a[j]);
			ans = tmp>ans? tmp:ans;
		}
	}
	cout << ans << endl;
	return 0;
}