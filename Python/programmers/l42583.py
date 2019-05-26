# -*- coding: utf-8 -*-

def solution(bridge_length, weight, truck_weights):
    answer, truck, on = 0, 0, 0
    que = [0 for _ in range(bridge_length)]
    while len(que) != 0:
        poll = que.pop(0)
        on -= poll
        if truck < len(truck_weights) and on+truck_weights[truck] <= weight:
            que.append(truck_weights[truck])
            on += truck_weights[truck]
            truck += 1
        elif truck != len(truck_weights):
            que.append(0)
        answer += 1
    return answer

ret = solution(2, 10, [7, 4, 5, 6])
print(ret)