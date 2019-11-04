package n9663;

import java.util.Scanner;

/**
 * 1차원 배열을 사용하여 문제를 푼다.
 * 배열의 각 요소는 각 인덱스 번호에 맞는 행에서 몇 번째의 위치에 퀸이 존재하는지 의미한다.
 * @author JungWoo
 *
 */
public class n9663_v2 {
	static int N;
	static int[] queens;
	static int count;

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		while (input.hasNext()) {
			N = Integer.parseInt(input.nextLine());
			queens = new int[N];
			count = 0;
			loop(queens, 0);
			System.out.println(count);
		}
		input.close();
	}
	
	public static void loop(int[] q, int pos) {
		boolean flag = true;
		if (pos == N) {
			count++;
			return;
		}
		for (int i = 0; i < N; i++) {
			q[pos] = i;
			flag = true;
			for (int j = 0; j < pos; j++)
				if (q[j] == q[pos] || Math.abs(q[j] - q[pos]) == pos - j) {
					flag = false;
					break;
				}
			if (flag)
				loop(q, pos+1);
		}
	}
}