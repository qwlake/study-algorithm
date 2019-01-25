package problems;
import java.util.Scanner;

public class week13_p2 {

	public static int[][] direction = { { -1, 0 }, { -1, 1 }, { 0, 1 }, { 1, 1 }, { 1, 0 }, { 1, -1 }, { 0, -1 },
			{ -1, -1 } };
	public static int N, R, C, maxH, maxT;
	public static int[][] map, distance, backDistance;
	public static boolean[][] isVisit;
	
	public static void backDistanceInit() {
		for (int i = 0; i < R; i++) {
			for (int j = 0; j < C; j++) {
				isVisit[i][j] = false;
				backDistance[i][j] = 100000;
			}
		}
	}

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		while (input.hasNext()) {
			String in[] = input.nextLine().split(" ");
			R = Integer.parseInt(in[0]);
			C = Integer.parseInt(in[1]);
			maxH = Integer.parseInt(in[2]);
			maxT = Integer.parseInt(in[3]);
			map = new int[R][C];
			isVisit = new boolean[R][C];
			distance = new int[R][C];
			backDistance = new int[R][C];

			for (int i = 0; i < R; i++) {
				in = input.nextLine().split("");
				for (int j = 0; j < C; j++) {
					map[i][j] = in[j].toCharArray()[0] - 65;
					isVisit[i][j] = false;
					distance[i][j] = 1000000;
					backDistance[i][j] = 1000000;
				}
			}

			distance[0][0] = 0;
			dijkstra(map, 0, 0, 0);
			print();
		}
	}

	public static void dijkstra(int[][] map, int startRow, int startCol, int opt)
	{
		int[][] distArr;
		if (opt == 0)
			distArr = distance;
		else
			distArr = backDistance;
		int row = startRow;
		int col = startCol;
		int nextRow, nextCol, weight, dist;
		while (isVisit[row][col] == false) {
			isVisit[row][col] = true;
			for (int i = 0; i < 8; i++) {
				nextRow = row + direction[i][0];
				nextCol = col + direction[i][1];
				if (0 <= nextRow && nextRow < R && 0 <= nextCol && nextCol < C) {
					weight = canClimb(row, col, nextRow, nextCol, opt);
					if (weight != -1)
						if (distArr[nextRow][nextCol] > distArr[row][col] + weight)
							distArr[nextRow][nextCol] = distArr[row][col] + weight;
				}
			}
			dist = 1000000;
			for (int i = 0; i < R; i++) {
				for (int j = 0; j < C; j++) {
					if (isVisit[i][j] == false && dist > distArr[i][j]) {
						dist = distArr[i][j];
						row = i;
						col = j;
					}
				}
			}
		}
	}

	public static int canClimb(int row, int col, int nextRow, int nextCol, int opt) {
		int diff = map[nextRow][nextCol] - map[row][col];
		if (0 < diff && diff <= maxH)
			return diff * diff;
		if (maxH * -1 <= diff && diff <= 0)
			return 1;
		return -1;
	}

	public static void print() {
		for (int i = 25; i >= 0; i--) {
			for (int j = 0; j < R; j++) {
				for (int k = 0; k < C; k++) {
					if (map[j][k] == i) {
						backDistance[j][k] = 0;
						dijkstra(map, j, k, 1);
						if (distance[j][k] + backDistance[0][0] <= maxT) {
							System.out.println(i);
							return;
						}
						backDistanceInit();
					}
				}
			}
		}
	}
}
