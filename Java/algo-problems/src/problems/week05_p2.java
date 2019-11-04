package problems;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.Scanner;

public class week05_p2 {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		while (input.hasNext()) {
			String word = "teemo";
			char[] wordCh = word.toCharArray();
			String[] line1 = input.nextLine().split(" ");
			int m = Integer.parseInt(line1[0]);
			int n = Integer.parseInt(line1[1]);
			String[][] line2 = new String[m][n];
			for (int i = 0; i < m; i++) {
				String temp = input.nextLine();
				for (int j = 0; j < n; j++)
					line2[i][j] = temp.substring(j, j + 1);
			}

			int[][] position = new int[2500][2];
			LinkedList<Integer> direction = new LinkedList<Integer>();

			int[] di = { -1, -1, -1, 0, 1, 1, 1, 0 };
			int[] dj = { -1, 0, 1, 1, 1, 0, -1, -1 };
			for (int i = 0; i < m; i++) {
				for (int j = 0; j < n; j++) {
					for (int dir = 0; dir < 8; dir++) {
						int row = i;
						int col = j;
						int t = 0;
						int wrong = 0;
						int totalWrong = 0;
						while (row >= 0 && row < m && col >= 0 && col < n && t < 5) {
							if ((line2[row][col].equalsIgnoreCase(word.substring(t, t + 1)) || wrong < 1) && totalWrong < 3) {
								if (!line2[row][col].equalsIgnoreCase(word.substring(t, t + 1))) {
									wrong++;
									totalWrong++;
								}
								else {
									wrong = 0;
								}
								if (totalWrong < 3) {
									row += di[dir];
									col += dj[dir];
									t++;
								}
							} else
								break;
						}
						if (t == 5) {
							position[direction.size()][0] = i;
							position[direction.size()][1] = j;
							direction.add(dir);
						}
					}
				}
			}

			int i = 0;
			int j = 0;
			Iterator<Integer> dirIter = direction.iterator();
			int dir = 0;
			try {
				int pIndex = 0;
				for (i = 0; i < m; i++) {
					for (j = 0; j < n; j++) {
						if (position[pIndex][0] == i && position[pIndex][1] == j) {
							int tempI = i;
							int tempJ = j;
							dir = dirIter.next();
							line2[i][j] = "#";
							for (int k = 0; k < 5; k++) {
								line2[tempI][tempJ] = "#";
								tempI += di[dir];
								tempJ += dj[dir];
							}
							pIndex++;
							j--;
						}
					}
				}
			} catch (Exception e) {
				//System.out.println(i + " " + dir + " " + j + " " + dir + "$$$$$");
				//System.out.println(e);
			}

			for (i = 0; i < m; i++) {
				for (j = 0; j < n; j++)
					System.out.print(line2[i][j]);
				System.out.println();
			}
		}
	}
}