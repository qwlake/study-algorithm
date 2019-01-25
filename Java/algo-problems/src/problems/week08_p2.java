package problems;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.LinkedList;
import java.util.List;
import java.util.Scanner;

public class week08_p2 {
	static List<Number> arr;

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		while (input.hasNext()) {
			int number = Integer.parseInt(input.nextLine());
			String[] tempString = input.nextLine().split(" ");
			arr = new ArrayList<Number>();
			LinkedList<Integer> path = new LinkedList<>();
			for (int i = 0; i < number; i++)
				arr.add(new Number(Integer.parseInt(tempString[i])));
			Collections.sort(arr, new NumberComp());
			for (int i = 0; i < number; i++) {
				path.add(arr.get(i).getNum());
				int ret = loop(arr.get(i), path);
				if (ret == 0)
					break;
				else {
					arr.get(i).pass = false;
					path.clear();
				}
			}
			for (int i : path) {
				System.out.print(i + " ");
			}
		}
	}

	public static int loop(Number num, List<Integer> path) {
		num.pass = true;
		int flag = 0;
		int ret = 0;
		for (int i = 0; i < arr.size(); i++) {
			if (!arr.get(i).pass) {
				flag = -1;
				break;
			}
		}

		if (flag == 0) {
			return flag; // All clear
		}
		
		for (int i = 0; i < arr.size(); i++) {
			if (!arr.get(i).pass && num.getNum() + 1 != arr.get(arr.indexOf(arr.get(i))).getNum()) {
				path.add(arr.get(arr.indexOf(arr.get(i))).getNum());
				ret = loop(arr.get(i), path);
				if (ret == -1) {
					arr.get(i).pass = false;
					path.remove(path.size() - 1);
				} else if (ret == 0)
					return 0;
			}
		}
		return flag;
	}
}

class Number {
	int num;
	boolean pass;

	Number(int num) {
		this.num = num;
		this.pass = false;
	}

	public int getNum() {
		return num;
	}
}

class NumberComp implements Comparator<Number> {
	int ret = 0;

	@Override
	public int compare(Number n1, Number n2) {
		if (n1.getNum() < n2.getNum()) {
			ret = -1;
		} else if (n1.getNum() == n2.getNum()) {
			ret = 0;
		} else if (n1.getNum() > n2.getNum()) {
			ret = 1;
		}
		return ret;
	}
}