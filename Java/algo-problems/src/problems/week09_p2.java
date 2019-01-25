package problems;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.Scanner;
 
public class week09_p2 {
    
    static LinkedList<String> record;
    
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        while (input.hasNext()) {
            String[] line = input.nextLine().split("");
            record = new LinkedList<>();
            int index = 0;
            loop(line, 0, line.length);
            Iterator<String> iter = record.iterator();
            while (iter.hasNext()) {
            	System.out.print(iter.next() + " ");
            	index++;
            	if (index == 100)
            		break;
            }
        }
    }
 
    public static void loop(String[] arr, int start, int end) {
        if (start == arr.length) {
            String temp = "";
            for (String pr : arr)
                temp += pr;
            if (record.isEmpty())
                record.add(temp);
            Iterator<String> iter = record.iterator();
            while (iter.hasNext())
                if (iter.next().equals(temp))
                    return;
            record.add(temp);
        } else {
            for (int i = start; i < end; i++) {
                swap(arr, start, i);
                loop(arr.clone(), start+1, end);
                reswap(arr, start, i);
            }
        }
    }
 
    public static void swap(String[] arr, int i, int j) {
        String temp = arr[j];
        for (int k = j-1 ; i <= k; k--)
        	arr[k+1] = arr[k];
        arr[i] = temp;
    }
    
    public static void reswap(String[] arr, int i, int j) {
        String temp = arr[i];
        for (int k = i+1 ; j >= k; k++)
        	arr[k-1] = arr[k];
        arr[j] = temp;
    }
}