package problems;
import java.util.Scanner;
import java.util.regex.Pattern;

public class week07_p1 {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		while (input.hasNext()) {
			String line = input.nextLine();
			String[] lineArr = line.split("");
			String result = "";
			String temp = "";
			int totalLen = lineArr.length;
			int engLen = 0;
			int hanLen = 0;
			int index = 0;
			for (String st : lineArr) {
				if (Pattern.matches("[a-zA-Z]", st)) {
					engLen++;
					result += st;
				} else if (Pattern.matches("[ê°?-?ž£]", st)) {
					hanLen++;
					temp += st;
				}
			}
			System.out.println(result + temp);
			System.out.println(engLen + " " + hanLen + " " + totalLen);
		}
	}
}
