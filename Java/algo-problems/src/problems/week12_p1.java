package problems;
import java.util.HashSet;
import java.util.Scanner;

public class week12_p1 {

	static int N;
	static int[] matrix;
	static int[] isMafia;
	static int[] shooted;
	static HashSet<Integer> totalSet;

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		while (input.hasNext()) {
			N = Integer.parseInt(input.nextLine());
			matrix = new int[N];
			isMafia = new int[N];
			shooted = new int[N];
			totalSet = new HashSet<>();
			int count = 0;
			for (int i = 0; i < N; i++) {
				matrix[i] = 0;
				shooted[i] = 0;
			}
			for (int i = 0; i < N; i++) {
				int n = Integer.parseInt(input.nextLine()) - 1;
				matrix[i] = n;
				shooted[n]++;
			}

			for (int i = 0; i < N; i++)
				if (shooted[i] == 0)
					isMafia[i] = 1;

			for (int i = 0; i < N; i++)
				if (shooted[i] == 0 && !totalSet.contains(i))
					checkMafia(i, 1);

			for (int i = 0; i < N; i++)
				if (!totalSet.contains(i))
					checkMafia(i, 0);

			for (int num : isMafia)
				count = (num == 1) ? count + 1 : count;

			System.out.println(count);
		}
	}

	public static void checkMafia(int person, int isM) {
		totalSet.add(person);
		if (isM % 2 == 1)
			isMafia[person] = 1;
		shooted[matrix[person]]--;
		if ((shooted[matrix[person]] == 0 || isM % 2 == 1) && !totalSet.contains(matrix[person]))
			checkMafia(matrix[person], isM + 1);
	}
}