package l42583;

import java.util.*;

class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int answer = 0;
        int truck = 0;
        int on = 0;
        Queue que = new LinkedList();
        for (int i = 0; i < bridge_length; i++) {
            que.offer(0);
        }
        while (!que.isEmpty()) {
            int temp = (int) que.poll();
            on -= temp;
            if (truck < truck_weights.length && on+truck_weights[truck] <= weight) {
                que.offer(truck_weights[truck]);
                on += truck_weights[truck];
                truck++;
            } else if (truck != truck_weights.length) {
                que.offer(0);
            }
            answer += 1;
        }
        return answer;
    }
}