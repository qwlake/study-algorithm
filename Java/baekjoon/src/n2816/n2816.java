package n2816;

import java.util.Scanner;

/**
 * KBS1 먼저 찾아 맨 위로 올린 뒤에 KBS2를 두 번째 위치로 옮김.
 * @author JungWoo
 *
 */
public class n2816 {

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		int N = Integer.parseInt(input.nextLine());
		String[] channels = new String[N];
		StringBuilder orders = new StringBuilder();
		int k1 = 0;
		int k2 = 0;
		for (int i = 0; i < N; i++) {
			channels[i] = input.nextLine().trim();
			if (channels[i].compareTo("KBS1") == 0)
				k1 = i;
			else if (channels[i].compareTo("KBS2") == 0)
				k2 = i;
		}
		k2 = (k1>k2)? k2+1:k2;
		for (int i = 0; i < k1; i++)
			orders.append("1");
		for (int i = 0; i < k1; i++)
			orders.append("4");
		for (int i = 0; i < k2; i++)
			orders.append("1");
		for (int i = 0; i < k2-1; i++)
			orders.append("4");
		System.out.println(orders);
		input.close();
	}
}