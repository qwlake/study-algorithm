package problems;
import java.util.Scanner;

public class week14_p1 {

	static int row, col;
	static int[][] map;
	static int[][] check;

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		String[] line = input.nextLine().split(" ");
		char[] chLine;
		row = Integer.parseInt(line[0]);
		col = Integer.parseInt(line[1]);
		map = new int[row][col];
		check = new int[row][col];

		int startRow, startCol, endRow = 0, endCol = 0;
		for (int i = 0; i < row; i++) {
			chLine = input.nextLine().toCharArray();
			for (int j = 0; j < col; j++) {
				map[i][j] = chLine[j] - 65;
				check[i][j] = 0;
				if (chLine[j] - 65 == -29) {
					startRow = i;
					startCol = j;
				} else if (chLine[j] - 65 == -27) {
					endRow = i;
					endCol = j;
				} else if (chLine[j] - 65 == -30) {
					map[i][j] = 1000000;
				}
			}
		}

		System.out.println(cost(map, endRow, endCol) + 56);

		// for (int i = 0; i < row; i++) {
		// for (int j = 0; j < col; j++) {
		// System.out.print(map[i][j]);
		// }
		// System.out.println();
		// }
	}

	public static int cost(int[][] map, int i, int j) {
		if (check[i][j] == 1) {
			return 1000000;
		}
		if (i == 0 && j == 0)
			return map[0][0];
		if (i == 0) {
			return cost(map, 0, j - 1) + map[0][j];
		}
		if (j == 0) {
			return cost(map, i - 1, 0) + map[i][0];
		}

		int a = 1000000, b = 1000000, c = 1000000, d = 1000000;

		if (check[i - 1][j] == 0) {
			check[i - 1][j] = 1;
			a = cost(map, i - 1, j);
		}
		if (check[i - 1][j] == 0) {
			check[i - 1][j] = 1;
			b = cost(map, i, j - 1);
		}
		if (check[i - 1][j] == 0) {
			check[i - 1][j] = 1;
			c = cost(map, i + 1, j);
		}
		if (check[i - 1][j] == 0) {
			check[i - 1][j] = 1;
			d = cost(map, i, j + 1);
		}

		return (Math.min(Math.min(a, b), Math.min(c, d)) + map[i][j]);
	}
}