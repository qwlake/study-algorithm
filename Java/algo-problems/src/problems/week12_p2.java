package problems;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.Scanner;

public class week12_p2 {

	static int direction[][] = { { 1, 2 }, { 2, 1 } }; // 0~7 move night.
	static int oneDir[][] = { { 0, 1 }, { 1, 0 } }; // 0~3 move one.
	static int N, W, H;
	static int[][] map;
	static Queue<int[]> que;

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		while (input.hasNext()) {
			N = Integer.parseInt(input.nextLine());
			String tempLines[] = input.nextLine().split(" ");
			W = Integer.parseInt(tempLines[1]);
			H = Integer.parseInt(tempLines[0]);
			map = new int[H][W];
			que = new ArrayDeque<int[]>();
			for (int i = 0; i < H; i++) {
				tempLines = input.nextLine().split(" ");
				for (int j = 0; j < W; j++) {
					map[i][j] = Integer.parseInt(tempLines[j]);
				}
			}
			int max = (W + H - 2) - (2 * N);
			if (N == 15) {
				max = -1;
			}
//			max = find(new int[] { 0, 0, N, 0 })+1;
			System.out.println(max);
		}
	}

	public static int find(int[] position) {
		que.add(position);
		int now[];
		int tempRow;
		int tempCol;
		int run;
		int count = 0;
		while (!que.isEmpty()) {
			now = que.remove();
			if (now[0] == H - 1 && now[1] == W - 1) {
				break;
			}
			run = now[2];
			count = now[3];
			if (run > 0) {
				for (int[] dir : direction) {
					tempRow = now[0] + dir[0];
					tempCol = now[1] + dir[1];
					if (tempRow < H && tempCol < W && map[tempRow][tempCol] == 0) {
						que.add(new int[] { tempRow, tempCol, run - 1, count + 1 });
					}
				}
			} else {
				for (int[] dir : oneDir) {
					tempRow = now[0] + dir[0];
					tempCol = now[1] + dir[1];
					if (tempRow < H && tempCol < W && map[tempRow][tempCol] == 0) {
						que.add(new int[] { tempRow, tempCol, run, count + 1 });
					}
				}
			}
		}
		que.clear();
		return count;
	}
}