package problems;
import java.util.LinkedList;
import java.util.Scanner;

public class week11_p1 {

	static int direction[][] = { { -2, 1 }, { -1, 2 }, { 1, 2 }, { 2, 1 }, { 2, -1 }, { 1, -2 }, { -1, -2 },
			{ -2, -1 } };
	static int N;
	static LinkedList<String> path;

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		while (input.hasNext()) {
			path = new LinkedList<>();
			N = Integer.parseInt(input.nextLine());
			String P[] = input.nextLine().split(" ");
			int startRow = Integer.parseInt(P[0]);
			int startCol = Integer.parseInt(P[1]);
			int pan[][] = new int[N][N];
			for (int i = 0; i < N; i++)
				for (int j = 0; j < N; j++)
					pan[i][j] = 0;
			pan[startRow][startCol] = 1;
			path.add(Integer.toString(startRow) + " " + Integer.toString(startCol));
			if (loop(pan, startRow, startCol) == true) {
				for (String print : path) {
					System.out.println(print);
				}
			} else {
				System.out.println("-1 -1");
			}
		}
	}

	public static boolean loop(int pan[][], int row, int col) {
		boolean flag = true;
		for (int dir[] : direction) {
			int tempRow = row + dir[0];
			int tempCol = col + dir[1];
			try {
				if (pan[tempRow][tempCol] == 0) {
					pan[tempRow][tempCol] = 1;
					path.add(Integer.toString(tempRow) + " " + Integer.toString(tempCol));
					if (loop(pan, tempRow, tempCol) == true)
						return true;
					pan[tempRow][tempCol] = 0;
					path.removeLast();
					flag = false;
				}
			} catch (Exception e) {}
		}
		if (flag == true) {
			for (int i = 0; i < N; i++)
				for (int j = 0; j < N; j++)
					if (pan[i][j] == 0)
						return false;
		}
		return flag;
	}
}