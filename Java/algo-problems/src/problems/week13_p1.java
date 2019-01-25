package problems;
import java.util.Scanner;

public class week13_p1 {

	static int N;
	static int[][] map;

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		N = Integer.parseInt(input.nextLine());
		map = new int[N][N];
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				map[i][j] = Integer.parseInt(input.nextLine());
			}
		}
		int times = Integer.parseInt(input.nextLine());
		for (int i = 0; i < times; i++) {
			String[] in = input.nextLine().split(" ");
			int start = Integer.parseInt(in[0]) - 1;
			int end = Integer.parseInt(in[1]) - 1;
			int[][] newMap = floyd(map);
			System.out.println(newMap[start][end]);
		}
	}

	public static int[][] floyd(int[][] map) {
		int i, j; /* dimension counters */
		int k; /* intermediate vertex counter */
		int through_k; /* distance through vertex k */
		for (k = 0; k < N; k++)
			for (i = 0; i < N; i++)
				for (j = 0; j < N; j++) {
					through_k = map[i][k] + map[k][j];
					if (through_k < map[i][j])
						map[i][j] = through_k;
				}
		return map;
	}
}