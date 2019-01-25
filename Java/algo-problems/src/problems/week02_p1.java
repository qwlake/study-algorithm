package problems;
import java.util.Scanner;

public class week02_p1 {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		while (input.hasNextLine()) {
			String s = input.nextLine().toUpperCase();
			int oper = -1;
			String prev = "";
			String curr = "";

			for (int i = 0; i < s.length(); i++) {
				int ch = (int) s.charAt(i);
				if (64 < ch && 75 > ch) {
					curr += ch - 65;
					if (oper != -1) {
						if (i >= s.length()-1 || s.charAt(i+1) == 'P' || s.charAt(i+1) == 'S' ||s.charAt(i+1) == 'T' ||s.charAt(i+1) == 'V') {
							if (oper == 80) {
								curr = Integer.toString(Integer.parseInt(prev) + Integer.parseInt(curr));
							} else if (oper == 83)
								curr = Integer.toString(Integer.parseInt(prev) - Integer.parseInt(curr));
							else if (oper == 84)
								curr = Integer.toString(Integer.parseInt(prev) * Integer.parseInt(curr));
							else if (oper == 86)
								curr = Integer.toString(Integer.parseInt(prev) / Integer.parseInt(curr));
							oper = -1;
						}
					}
				} else if (s.charAt(i) == 'P' || s.charAt(i) == 'S' ||s.charAt(i) == 'T' ||s.charAt(i) == 'V') {
					if (oper != -1) {
						curr = "Error";
						break;
					}
					oper = ch;
					prev = curr;
					curr = "";
				}
			}
			if (curr == "")
				System.out.println("Error");
			else
				System.out.println(curr);
		}
	}
}