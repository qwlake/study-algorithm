package problems;

import java.util.Scanner;

public class week01_p2 {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);

        while (input.hasNextLine()) {
            String s = input.nextLine().trim();
            if (s.contains("x")) {
            	String num = s.substring(2);
            	int toDec = Integer.parseInt(num, 16);
            	System.out.println(toDec);
            } else {
            	int num = Integer.parseInt(s);
            	String toHex = Integer.toHexString(num);
            	toHex = "0x" + toHex.toUpperCase();
            	System.out.println(toHex);
            }
        }
	}
}
