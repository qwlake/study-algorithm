package n13574;

import java.util.Scanner;

public class n13574 {
	static int n;
	static int max;
	static int[][] arrA;
	static int[][] arrB;
	public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        while (input.hasNextLine()) {
            String[] inputLine = input.nextLine().split(" ");
            n = Integer.parseInt(inputLine[0]);
            int k = Integer.parseInt(inputLine[1]);
            max = (int) Math.pow(2, k);
            arrA = new int[n][];
            arrB = new int[n][];
            loop(n, 1);
        }
        input.close();
    }
	
	public static void loop(int n, int num) {
		if (n == 0)
			return;
		for (int i = num+1; i < max; i++) {
			loop(n-1, i);
		}
	}
}
