package n3006;

import java.util.LinkedList;
import java.util.Scanner;

public class n3006 {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		int N = Integer.parseInt(input.nextLine());
		LinkedList<Integer> read = new LinkedList<Integer>();
		int[] result = new int[N];
		for (int i = 0; i < N; i++)
			read.add(Integer.parseInt(input.nextLine())-1);
		for (int i = 0; i < N/2; i++) {
			int idx = read.indexOf(i);
			result[i*2] = Math.abs(idx-i);
			read.add(i, read.remove(idx));
			
			idx = read.indexOf(N-i-1);
			result[i*2+1] = Math.abs(idx-(N-i-1));
			read.add(N-i-1, read.remove(idx));
		}
		for (int r : result)
			System.out.println(r);
	}
}