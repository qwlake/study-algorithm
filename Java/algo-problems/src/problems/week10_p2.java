package problems;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.List;
import java.util.Scanner;

public class week10_p2 {
	static LinkedList<Integer> primes;
	static List<String> numbers;

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		while (input.hasNext()) {
			primes = new LinkedList<>();
			int N = Integer.parseInt(input.nextLine());
			String[] temps = input.nextLine().split(" ");
			numbers = new ArrayList<>();
			for (String temp : temps)
				numbers.add(temp);
			search(numbers, "");
			if (primes.isEmpty()) {
				System.out.println("No Prime!");
			} else {
				Collections.sort(primes);
				Iterator<Integer> iter = primes.iterator();
				while (iter.hasNext())
					System.out.print(iter.next() + " ");
				System.out.println();
			}
		}
	}

	public static void add(int prime) {
		if (!primes.contains(prime))
			primes.add(prime);
	}

	public static void search(List<String> numbers, String num) {
		if (numbers.isEmpty()) {
			return;
		} else {
			String temp = "";
			String[] clone = numbers.toArray(new String[numbers.size()]);
			for (int i = 0; i < clone.length; i++) {
				temp = num + String.valueOf(clone[i]);
				if (checkPrime(Integer.parseInt(temp))) {
					add(Integer.parseInt(temp));
					numbers.remove(clone[i]);
					search(numbers, temp);
					numbers.add(clone[i]);
				} else {
					numbers.remove(clone[i]);
					search(numbers, temp);
					numbers.add(clone[i]);
				}
			}
		}
	}

	public static boolean checkPrime(int num) {
		boolean isPrime = false;
		int sq = (int) Math.sqrt(num);
		if (num == 2 || num == 3)
			return true;
		if (num % sq != 0)
			isPrime = true;
		else
			isPrime = false;
		for (int i = 3; i <= sq; i += 2) {
			if (num % 2 == 0 || num % i == 0) {
				isPrime = false;
				break;
			} else {
				isPrime = true;
			}
		}
		return isPrime;
	}
}