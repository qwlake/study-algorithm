package problems;

import java.util.Scanner;

public class week01_p3 {
	public static void main(String[] args) {
        Scanner s = new Scanner(System.in);

        while (s.hasNextInt()) {
            int n = s.nextInt();
            int x = s.nextInt();

            if (cycleHas(n, x)) System.out.println("Y");
            else System.out.println("N");
        }
    }

	private static boolean cycleHas(int n, int x) {
		while (n != 1) {
			if (n == x)
				return true;
			if (n%2 == 1)
				n = n*3 + 1;
			else
				n /= 2;
		}
		return false;
	}
}
