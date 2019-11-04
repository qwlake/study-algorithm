package n2816;

import java.util.Scanner;

/**
 * KBS1이나 KBS2 중 먼저 오는 것을 맨 위로 올린 뒤에 남은 것을 첫 번째 혹은 두 번째 위치로 옮김.
 * @author JungWoo
 *
 */
public class n2816_v2 {

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		int N = Integer.parseInt(input.nextLine());
		String[] channels = new String[N];
		StringBuilder orders = new StringBuilder();
		int k1 = 0;
		int k2 = 0;
		int temp;
		for (int i = 0; i < N; i++) {
			channels[i] = input.nextLine().trim();
			if (channels[i].compareTo("KBS1") == 0)
				k1 = i;
			else if (channels[i].compareTo("KBS2") == 0)
				k2 = i;
		}
		if (k1 > k2) {
			temp = k1;
			k1 = k2;
			k2 = temp;
			temp = 0;
		} else {
			temp = 1;
		}
		for (int i = 0; i < k1; i++)
			orders.append("1");
		for (int i = 0; i < k1; i++)
			orders.append("4");
		for (int i = 0; i < k2; i++)
			orders.append("1");
		k2 = (temp == 0)? k2+1:k2;
		for (int i = 0; i < k2-1; i++)
			orders.append("4");
		System.out.println(orders);
		input.close();
	}
}