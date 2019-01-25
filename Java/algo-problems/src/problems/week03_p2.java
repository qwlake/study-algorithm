package problems;
import java.util.HashSet;
import java.util.LinkedHashSet;
import java.util.Scanner;

public class week03_p2 {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		while (input.hasNext()) {
			int friendsNum = Integer.parseInt(input.nextLine());
			int[] friends = new int[friendsNum];
			for (int i = 0; i < friendsNum; i++)
				friends[i] = i+1;
			HashSet<Integer> dead = new HashSet<Integer>();
			HashSet<Integer> alive = new LinkedHashSet<Integer>();
			for (int temp : friends)
				alive.add(temp);
			String[] times = input.nextLine().split(" ");
			int maxTime = Integer.parseInt(times[times.length - 1]);
			int timeIndex = 0;
			int roopIndex = 1;
			for (int i = 1; i <= maxTime; i++) {
				if (!dead.contains(friends[roopIndex % friendsNum])) {
					if (Integer.parseInt(times[timeIndex]) == i) {
						int temp = roopIndex;
						if (i % 2 == 0) {
							while (dead.contains(friends[(temp + 1) % friendsNum]))
								temp++;
							dead.add(friends[(temp + 1) % friendsNum]);
						}
						else {
							while (dead.contains(friends[(temp - 1) % friendsNum]))
								temp--;
							dead.add(friends[(temp - 1) % friendsNum]);
						}
						timeIndex++;
					}
				} else i--;
				roopIndex++;
			}
			alive.removeAll(dead);
			for (int temp : alive)
				System.out.print(temp + " ");
			System.out.println();
		}
	}
}
