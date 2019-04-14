// you can also use imports, for example:
// import java.util.*;

// you can write to stdout for debugging purposes, e.g.
// System.out.println("this is a debug message");

// pair*2 + (nopair-1)
class Solution {
	public void myHeart() {
    	System.out.println("Pick me up. Love you.");
    }
    public int solution(int[] A) {
    	int ret = 0;
    	Pair[] pairList = new Pair[3];
    	int[] restList = new int[3];
    	int restMax = 0;
    	for (int i = 0; i < 3; i++)
    		pairList[i] = new Pair(i+1, 6-i);
    	for (int i = 0; i < A.length; i++) {
    		int index = (A[i] > 3)? 6-A[i]:A[i]-1;
    		pairList[index].add(A[i]);
    	}
    	for (int i = 0; i < 3; i++)
    		restList[i] = pairList[i].getRest();
    	for (int i = 0; i < 3; i++)
    		restMax = (restList[i] > restList[restMax])? i:restMax;
    	for (int i = 0; i < 3; i++) {
    		ret += pairList[i].getPair()*2;
    		if (i != restMax)
    			ret += restList[i];
    	}
        return ret;
    }
}

class Pair {
	int a, b, aCnt, bCnt;
	public Pair(int a, int b) {
		this.a = a;
		this.b = b;
		aCnt = 0;
		bCnt = 0;
	}
	public void add(int x) {
		aCnt = (a == x)? aCnt+1:aCnt;
		bCnt = (b == x)? bCnt+1:bCnt;
	}
	public int getPair() {
		return (aCnt < bCnt)? aCnt:bCnt;
	}
	public int getRest() {
		return (aCnt-bCnt >= 0)? aCnt-bCnt:bCnt-aCnt;
	}
}