package problems;
import java.util.Scanner;

public class week11_p2 {

	static int[][] friends;

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		while (input.hasNext()) {
			String inputs[] = input.nextLine().split(" ");
			int K = Integer.parseInt(inputs[0]);
			int N = Integer.parseInt(inputs[1]);
			int F = Integer.parseInt(inputs[2]);
			friends = new int[N][N];
			for (int i = 0; i < N; i++)
				friends[i][i] = 1;

			for (int i = 0; i < F; i++) {
				String temp[] = input.nextLine().split(" ");
				int first = Integer.parseInt(temp[0]);
				int second = Integer.parseInt(temp[1]);
				friends[first - 1][second - 1] = 1;
				friends[second - 1][first - 1] = 1;
			}

			int result[] = check(K, N);
			if (result == null) {
				System.out.println("-1");
			} else {
				int count = 0;
				for (int i = 0; i < N; i++) {
					if (result[i] == 1) {
						System.out.println(i + 1);
						count++;
					}
					if (count >= K)
						break;
				}
			}
		}
	}

	public static int[] check(int K, int N) {
		for (int[] f : friends) {
			int[] temp = f.clone();
			for (int i = 0; i < N; i++)
				if (temp[i] != 0)
					for (int k = 0; k < N; k++)
						temp[k] = (temp[k] == friends[i][k]) ? temp[k]:0;

			int count = 0;
			for (int i = 0; i < N; i++)
				if (temp[i] == 1)
					count++;
			if (count >= K)
				return temp;
		}
		return null;
	}
}