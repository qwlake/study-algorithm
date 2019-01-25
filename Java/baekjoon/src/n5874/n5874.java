package n5874;

import java.util.Scanner;

/**
 * "("의 개수와 ")"의 개수를 찾아 서로 곱한뒤 더한다.
 * @author JungWoo
 *
 */
public class n5874 {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		while (input.hasNext()) {
			String[] line = input.nextLine().split("");
			int[] legs = new int[line.length];
			int[] check = new int[line.length];
			int total = 0;
			int decide = 0;
			int legsIndex = 0;
			int arg = 0;
			for (int i = 0; i < line.length; i++) {
				arg = (line[i].compareTo("(") == 0)? 1:-1;
				if (decide == arg) {
					legs[legsIndex] += arg;
				} else {
					if (legs[legsIndex] != 0)
						legsIndex++;
					decide = arg;
				}
			}
			int legsCount = (legs[legsIndex] == 0)? legsIndex:legsIndex+1;
			int count = 0;
			for (int i = 0; i < legsCount; i++) {
				if (legs[i] > 0 && check[i] == 0) {
					count = 0;
					legsIndex = i;
					check[i] = 1;
					for (int j = legsIndex+1 ; j < legsCount; j++) {
						if (legs[j] < 0) {
							count -= legs[j];
							check[j] = -1;
						}
					}
					total += legs[i] * count;
				}
			}
			System.out.println(total);
		}
		input.close();
	}
}