package problems;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;

public class week03_p3 {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		int ttt = 0;
		while (input.hasNext()) {
			int N = Integer.parseInt(input.nextLine());
			String[] Xi = input.nextLine().split(" ");
			String[] proccess = input.nextLine().split("");
			String result = "";
			Integer[] mushs = new Integer[N];
			for (int i = 0; i < N; i++)
				mushs[i] = Integer.parseInt(Xi[i]);
			ArrayList<Integer> list = new ArrayList<>(Arrays.asList(mushs));
			int pCount = 0;
			for (String p : proccess) {
				if (p.equals("R")) {
					Collections.reverse(list);
					pCount++;
				} else if (p.equals("B")) {
					list.remove((Object) Collections.max(list));
					pCount++;
				} else if (p.equals("S")) {
					list.remove((Object) Collections.min(list));
					pCount++;
				} else {
					result = "Wrong Command!";
					break;
				}
				if (list.isEmpty() && proccess.length > pCount) {
					result = "No mushrooms!";
					break;
				}
				else if (list.isEmpty() && proccess.length <= pCount) {
					result = "Empty!";
					break;
				}
			}
			if (result.equals(""))
				for (int i = 0; i < list.size(); i++)
					result += list.get(i) + " ";
			System.out.println(result);
		}
	}
}
