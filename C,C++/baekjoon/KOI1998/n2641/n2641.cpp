#include <iostream>

using namespace std;

int N, M, tmp;
int **s, **arr, *answer;

int main() {
	cin >> N;
	s = new int*[2] {new int[2*N], new int[2*N]};
	for (int i = 0; i < N; i++)		// 주어진 도형
		cin >> s[0][i];
	for (int i = N; i < 2*N; i++)
		s[0][i] = s[0][i-N];
	for (int i = 0; i < N; i++) {	// 주어진 도형의 반대로 도는 도형 저장
		tmp = s[0][N-1-i]+2;
		s[1][i] = (tmp>4)? (tmp%4):(tmp);
	}
	for (int i = N; i < 2*N; i++)
		s[1][i] = s[1][i-N];
	cin >> M;
	arr = new int*[M];
	for (int i = 0; i < M; i++) {
		arr[i] = new int[N];
		for (int j = 0; j < N; j++)
			cin >> arr[i][j];
	}

	answer = new int[M];
	int answerIdx = 0;
	for (int i = 0; i < M; i++) {	// 테스트 도형들
		for (int two = 0; two < 2; two++) {
			for (int j = 0; j < N; j++) {	// 샘플 도형 순환
				int isPassed = 0;
				for (int k = 0; k < N; k++) {	// 검증
					if (s[two][j+k] != arr[i][k]) {
						break;
					}
					isPassed = k;
				}
				if (isPassed+1 == N) {
					answer[answerIdx++] = i;
				}
			}
			if (answer[answerIdx-1] == i) break;
		}
	}

	cout << answerIdx << endl;
	for (int i = 0; i < answerIdx; i++) {
		for (int j = 0; j < N; j++)
			cout << arr[answer[i]][j] << " ";
		cout << endl;
	}
		
	return 0;
}