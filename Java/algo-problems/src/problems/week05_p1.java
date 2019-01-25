package problems;
import java.util.Scanner;

public class week05_p1 {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		while (input.hasNext()) {
			String line1 = input.nextLine();
			String line2 = input.nextLine();
			int count = 0;
			if (line1.length() > line2.length()) {
				String temp = line1;
				line1 = line2;
				line2 = temp;
			}
			int lenLine1 = line1.length();
			int lenLine2 = line2.length();

			for (int i = 0; i < line1.length(); i++) {
				for (int j = 0; j < line2.length(); j++) {
					if (line2.contains(line1.substring(i, i + 1))) {
						count++;
						line2 = line2.replaceFirst(line1.substring(i, i + 1), "");
						break;
					}
				}
			}

			System.out.println(lenLine1 + lenLine2 - (count * 2));
		}
	}
}
