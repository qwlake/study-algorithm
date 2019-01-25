package n5874;

import java.util.Scanner;

/**
 * "("의 개수를 ")"를 찾은 개수만큼 더한다.
 * 다음에 오는 ")"를 찾으면 그 전에 있던 모든 "(" 개수를 더하기 때문에 모든 경우의 수를 파악할 수 있다.
 * @author JungWoo
 *
 */
public class n5874_v2 {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		while (input.hasNext()) {
			String[] line = input.nextLine().split("");
			int count = 0;
			int sum = 0;
			for (int i = 1; i < line.length; i++) {
				if (line[i].compareTo(line[i-1]) == 0) {
					if (line[i].compareTo("(") == 0)
						count++;
					else
						sum += count;
				}
			}
			System.out.println(sum);
		}
		input.close();
	}
}
