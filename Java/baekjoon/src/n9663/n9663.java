package n9663;

import java.util.Scanner;

/**
 * 기본적으로 2차원 배열을 사용해서 문제를 푼다.
 * 하지만 루프를 너무 많이 도는지 메모리 초과가 난다.
 * @author JungWoo
 *
 */
public class n9663 {
	static int number;
	static int[][] pan;
	static int count;

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		while (input.hasNext()) {
			number = Integer.parseInt(input.nextLine());
			pan = new int[number][number];
			count = 0;
			for (int i = 0; i < number; i++)
				for (int j = 0; j < number; j++)
					pan[i][j] = 0;
			loop(0, 0, 0);
			System.out.println(count);
		}
		input.close();
	}

	public static void loop(int row, int col, int queens) {
		if (queens == number) {
			count++;
			return;
		} else if (row < number) {
			for (int i = 0; i < number; i++) {
				if (pan[row][i] >= 0) {
					possibleChange(row, i, -1);
					loop(row + 1, 0, queens + 1);
					possibleChange(row, i, 1);
				}
			}
		}
	}

	public static void possibleChange(int row, int col, int sub) {
		int[][] pos = { { -1, 1 }, { 1, 1 }, { 1, -1 }, { -1, -1 } };
		for (int i = 0; i < number; i++)
			pan[row][i] += sub;
		for (int i = 0; i < number; i++)
			pan[i][col] += sub;
		for (int i = 0; i < pos.length; i++) {
			int tempRow = row;
			int tempCol = col;
			while (tempRow >= 0 && tempRow < number && tempCol >= 0 && tempCol < number) {
				pan[tempRow][tempCol] += sub;
				tempRow += pos[i][0];
				tempCol += pos[i][1];
			}
		}
		for (int i = 0; i < 5; i++)
			pan[row][col] -= sub;
	}
}