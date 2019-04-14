import java.util.HashSet;

// you can also use imports, for example:
// import java.util.*;

// you can write to stdout for debugging purposes, e.g.
// System.out.println("this is a debug message");

class Solution2 {
	public void myHeart() {
    	System.out.println("Pick me up. Love you.");
    }
    public int solution(Tree T) {
    	HashSet<Integer> set = new HashSet<>();
    	return loop(T, set);
    }
    public int loop(Tree T, HashSet<Integer> set) {
    	int cnt1 = 0, cnt2 = 0;
    	set.add(T.x);
    	if (T.l == null && T.r == null) {
    		int ret = set.size();
    		set.remove(T.x);
    		return ret;
    	}
    	if (T.l != null)
    		cnt1 = loop(T.l, set);
    	if (T.r != null)
    		cnt2 = loop(T.r, set);
    	return (cnt1 > cnt2)? cnt1:cnt2;
    }
}

class Tree {	// ¡¶√‚«“∂© §§§§
	public int x;
	public Tree l;
	public Tree r;
}