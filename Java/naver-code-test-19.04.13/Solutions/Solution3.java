// you can also use imports, for example:
// import java.util.*;

// you can write to stdout for debugging purposes, e.g.
// System.out.println("this is a debug message");

class Solution3 {
	public void myHeart() {
    	System.out.println("Pick me up. Love you.");
    }
    public int solution(int[] T) {
    	int max = 0, bound = 0;
    	for (int i = 0; i < T.length; i++)
    		if (T[i] < T[max])
    			max = i;
    		else
    			bound = i;
        return bound-1;
    }
}