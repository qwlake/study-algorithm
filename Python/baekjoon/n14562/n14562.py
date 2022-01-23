import sys
from collections import deque
input1 = sys.stdin.readline


def fun1(q):
    cnt = 1
    while q:
        popped = q.popleft()
        nxts = []
        for s, t in popped:
            s1, t1 = s * 2, t + 3
            if s1 == t1:
                return cnt
            elif s1 < t1:
                nxts.append([s1, t1])
            s2, t2 = s + 1, t
            if s2 == t2:
                return cnt
            elif s2 < t2:
                nxts.append([s2, t2])
        q.append(nxts)
        cnt += 1


def main():
    for _ in range(int(input1())):
        print(fun1(deque([[list(map(int, input1().split()))]])))


if __name__ == "__main__":
    main()
