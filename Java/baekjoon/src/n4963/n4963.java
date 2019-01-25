package n4963;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

public class n4963 {
	static int[][] direction = { { -1, 0 }, { -1, 1 }, { 0, 1 }, { 1, 1 }, { 1, 0 }, { 1, -1 }, { 0, -1 }, { -1, -1 } };
	static int row;
	static int col;
	static int map[][];

	public static void main(String[] args) throws IOException {
		BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
		while (true) {
			String temp[] = input.readLine().split(" ");
			row = Integer.parseInt(temp[1]);
			col = Integer.parseInt(temp[0]);
			if (row == 0 && col == 0)
				break;
			map = new int[row][col];

			for (int i = 0; i < row; i++) {
				temp = input.readLine().split(" ");
				for (int j = 0; j < col; j++)
					map[i][j] = Integer.parseInt(temp[j]);
			}

			int count = startMerge();
			System.out.println(count);
		}
		input.close();
	}
    
    public static int startMerge() {
        Queue<int[]> que = new LinkedList<>();
		int count = 0;
		for (int i = 0; i < row; i++) {
			for (int j = 0; j < col; j++) {
				if (map[i][j] == 1) {
					merge(que, new int[] { i, j });
					count++;
				}
			}
		}
		return count;
	}

	public static void merge(Queue<int[]> que, int[] startPos) {
		que.add(startPos);
		map[startPos[0]][startPos[1]] = 0;
		int now[];
		int tempRow;
		int tempCol;
		while (!que.isEmpty()) {
			now = que.remove();
			for (int[] dir : direction) {
				tempRow = now[0] + dir[0];
				tempCol = now[1] + dir[1];
				if (0 <= tempRow && tempRow < map.length && 0 <= tempCol && tempCol < map[0].length
						&& map[tempRow][tempCol] == 1) {
					que.add(new int[] { tempRow, tempCol });
					map[tempRow][tempCol] = 0;
				}
			}
		}
		que.clear();
	}
}