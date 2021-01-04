import sys
from collections import deque

for _ in range(int(sys.stdin.readline())):
    lst = []
    for i in range(int(sys.stdin.readline())):
        h, w = list(map(int, sys.stdin.readline().strip().split()))
        lst.append((h,w,i))
    sorted_h = sorted(lst, key=lambda x: (x[0], x[1]))
    sorted_w = sorted(lst, key=lambda x: (x[1], x[0]))
    answer = []
    for i in range(len(lst)):
        for j in range(len(sorted_h)):
            if sorted_h[j][2] == i:
                continue
            if sorted_h[j][0] < lst[i][0] and sorted_h[j][1] < lst[i][1]:
                answer.append(sorted_h[j][2]+1)
                break
        if len(answer) != i+1:
            answer.append(-1)
    print(' '.join(list(map(str, answer))))