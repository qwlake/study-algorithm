package problems;
import java.util.Scanner;

public class week09_p1 {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		while (input.hasNext()) {
			int number = Integer.parseInt(input.nextLine());
			String st = "1";
	        for(int i=0; i<number; i++) {
	        	if (i == number-1)
	            	System.out.println(st);
	            String temp = "";
	            int count = 1;
	            for(int j = 0; j < st.length(); j++) {
	                if(j == st.length()-1 || st.charAt(j) != st.charAt(j+1)) {
	                	temp = temp + st.charAt(j)+count;
	                    count = 1;
	                } else {
	                	count++;
	                }
	            }
	            st = temp;
	        }
		}
	}
}