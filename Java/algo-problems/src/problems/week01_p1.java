package problems;

import java.util.Scanner;

public class week01_p1 {
	public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        while (input.hasNextLine()) {
            String s = input.nextLine();
            String[] arr = s.trim().split(" ");
            int letters = s.replaceAll(" ", "").length();
            int words = arr.length;
            System.out.println(words + " " + letters);
        }
    }
}
