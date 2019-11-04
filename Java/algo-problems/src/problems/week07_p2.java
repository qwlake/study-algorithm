package problems;
import java.util.LinkedHashMap;
import java.util.Scanner;

public class week07_p2 {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		while (input.hasNext()) {
			String master = "the quick brown fox jumps over the lazy dog";
			String[] masterArr = master.replaceAll(" ", "").split("");
			LinkedHashMap<String, String> masterMap = new LinkedHashMap<String, String>();
			LinkedHashMap<String, String> myMap = new LinkedHashMap<String, String>();

			String line1 = input.nextLine();
			String line2 = input.nextLine();
			String line3 = input.nextLine();

			String[] line1Arr = line1.replace(" ", "").split("");
			for (int i = 0; i < line1Arr.length; i++)
				if (!line1Arr[i].equals("?"))
					masterMap.put(masterArr[i], line1Arr[i]);

			String[] before = line2.split(" ");
			String[] after = line3.split(" ");
			String bfSt = "";
			String afSt = "";
			
			for (String ms : masterMap.keySet())
				for (String bf : before)
					for (String af : after)
						if (bf.length() == af.length() && bf.contains(ms) && af.contains(masterMap.get(ms)))
							for (int i = 0; i < bf.length(); i++)
								if (bf.substring(i, i+1).equals(ms) && af.substring(i, i+1).equals(masterMap.get(ms)))
									for (int j = 0; j < bf.length(); j++)
										myMap.put(bf.substring(j, j+1), af.substring(j, j+1));
			
			masterMap.putAll(myMap);
			myMap.clear();
			boolean flag = false;

			for (String bf : before) {
				for (String af : after) {
					if (bf.length() != af.length())
						continue;
					for (int i = 0; i < bf.length(); i++) {
						bfSt = bf.substring(i, i + 1);
						afSt = af.substring(i, i + 1);
						if ((masterMap.containsKey(bfSt) && !masterMap.get(bfSt).equals(afSt))
								|| (myMap.containsKey(bfSt) && !myMap.get(bfSt).equals(afSt))
								|| (masterMap.containsValue(afSt) && !bfSt.equals(getKey(masterMap, afSt)))
								|| (myMap.containsValue(afSt) && !bfSt.equals(getKey(myMap, afSt)))) {
							for (int j = 0; j < i; j++)
								myMap.remove(bf.substring(j, j + 1));
							flag = true;
							break;
						} else if (!masterMap.containsKey(bfSt) && !myMap.containsKey(bfSt)) {
							myMap.put(bfSt, afSt);
						}
					}
					if (!flag)
						break;
				}
			}

			for (int i = 0; i < master.length(); i++) {
				String temp = master.substring(i, i + 1);
				if (masterMap.containsKey(temp)) {
					System.out.print(masterMap.get(temp));
				} else if (myMap.containsKey(temp)) {
					System.out.print(myMap.get(temp));
				} else {
					System.out.print(line1.substring(i, i + 1));
				}
			}
		}
	}

	public static Object getKey(LinkedHashMap<String, String> m, Object value) {
		for (Object o : m.keySet())
			if (m.get(o).equals(value))
				return o;
		return null;
	}
}
