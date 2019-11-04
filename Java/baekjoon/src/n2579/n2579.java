package n2579;

import java.util.Scanner;

/**
 * 제대로 작동되지 않는다. DP를 사용사여 풀어야 한다.
 * @author JungWoo
 *
 */
public class n2579 {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		int N = Integer.parseInt(input.nextLine());
		int[] steps = new int[N];
		int sum = 0;
		int con = 0;
		for (int i = 0; i < N; i++)
			steps[i] = Integer.parseInt(input.nextLine());
		int index = 0;
		try {
			while (index < N) {
				//System.out.println(steps[index] + " " + index + " " + con);
				sum += steps[index];
				if (con == 1) {
					index += 2;
					con = 0;
				} else if (index + 3 == N) {
					index += 2;
				} else if (index + 2 == N || steps[index + 1] > steps[index + 2]) {
					index++;
					con++;
				} else {
					index += 2;
				}
			}
		} catch (Exception e) {
			// TODO: handle exception
		}
		System.out.println(sum);
		input.close();
	}
}