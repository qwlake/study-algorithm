package problems;
import java.util.Scanner;

public class week10_p1 {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		while (input.hasNext()) {
			search(input.nextInt(), 0, "");
		}
	}

	public static void search(int n, int count, String num) {
		if (count == n) {
			System.out.println(num);
		} else {
			String temp = "";
			for (int i = 0; i < 10; i++) {
				temp = num+String.valueOf(i);
				if (checkPrime(Integer.parseInt(temp)))
					search(n, count+1, temp);
			}
		}
	}

	public static boolean checkPrime(int num) {
		int count = 0;
		boolean ret = (num < 2)? false:true;
		for (int i = 1; i < num; i++) {
			if (num % i == 0)
				count++;
			if (count > 1) {
				ret = false;
				break;
			}
		}
		return ret;
	}
}