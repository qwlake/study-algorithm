package problems;
import java.util.Comparator;
import java.util.LinkedHashMap;
import java.util.Map;
import java.util.Scanner;
import java.util.TreeMap;

public class week02_p2 {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		while (input.hasNextLine()) {
			Map<String, Integer> map = new LinkedHashMap<String, Integer>();
			String[] firstLine = input.nextLine().split(" ");
			int n = Integer.parseInt(firstLine[0]);
			int m = Integer.parseInt(firstLine[1]);
			String[] secondLine = input.nextLine().split(" ");

			for (String str : secondLine) {
				if (map.containsKey(str))
					map.replace(str, map.get(str)+1);
				else if (Integer.parseInt(str) <= m)
					map.put(str, 1);
			}
			
			TreeMap<String,Integer> sortedMap = new TreeMap<String,Integer>(new ValueComparator(map));
			sortedMap.putAll(map);
			for (String key : sortedMap.keySet())
				for (int i = 0; i < map.get(key); i++)
					System.out.print(key + " ");
			System.out.println();
		}
	}
}

class ValueComparator implements Comparator<String> {

    Map<String, Integer> map;
    public ValueComparator(Map<String, Integer> map) {
        this.map = map;
    }

    public int compare(String a, String b) {
        if (map.get(a) <= map.get(b))
            return 1;
        else
            return -1;
    }
}