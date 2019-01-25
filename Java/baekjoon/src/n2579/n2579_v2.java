package n2579;

import java.util.Scanner;

/**
 * DP로 구현하였다.
 * @author JungWoo
 *
 */
public class n2579_v2 {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		int N = Integer.parseInt(input.nextLine());
		int[] steps = new int[N];
		int[][] matrix = new int[N+1][3];
		for (int i = 0; i < N; i++)
			steps[i] = Integer.parseInt(input.nextLine());
		for (int i = 1; i < N+1; i++) {
			matrix[i][0] = (matrix[i-1][1] > matrix[i-1][2])? matrix[i-1][1]:matrix[i-1][2];
			matrix[i][1] = matrix[i-1][0] + steps[i-1];
			matrix[i][2] = matrix[i-1][1] + steps[i-1];
		}
		System.out.println((matrix[N][1] > matrix[N][2])? matrix[N][1]:matrix[N][2]);
		
//		for (int i = 0; i < N+1; i++) {
//			for (int j = 0; j < 3; j++) {
//				System.out.print(matrix[i][j] + " ");
//			}
//			System.out.println();
//		}
		input.close();
	}
}