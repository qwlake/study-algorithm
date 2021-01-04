import sys
from collections import deque

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    list1 = list(map(int, sys.stdin.readline().strip().split()))
    even, odd = [], []
    for i in range(len(list1)):
        if list1[i] % 2 == 0:
            even.append(list1[i])
        else:
            odd.append(list1[i])
    even = deque(sorted(even, reverse=True))
    odd = deque(sorted(odd, reverse=True))
    lists = [even, odd]
    idx = 0
    cnts = [0, 0]
    while True:
        l1, l2 = lists[idx%2], lists[(idx+1)%2]
        if len(l1) != 0 and len(l2) != 0:
            if l1[0] > l2[0]:
                cnts[idx%2] += l1.popleft()
            else:
                l2.popleft()
        elif len(l1) == 0:
            if len(l2) == 0:
                break
            else:
                l2.popleft()
        elif len(l2) == 0:
            cnts[idx%2] += l1.popleft()
        idx += 1
    if cnts[0] < cnts[1]:
        print("Bob")
    elif cnts[0] > cnts[1]:
        print("Alice")
    else:
        print("Tie")