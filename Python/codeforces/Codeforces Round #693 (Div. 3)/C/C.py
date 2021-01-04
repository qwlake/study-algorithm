import sys

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    list1 = list(map(int, sys.stdin.readline().strip().split()))
    score = [0]*(n+1)
    for i in range(len(list1)-1, -1, -1):
        j = i
        tmp = 0
        while True:
            tmp += list1[j]
            j = j + list1[j]
            if j >= len(list1):
                score[i] = tmp
                break
            elif score[j] != 0:
                score[i] = tmp + score[j]
                break
    print(max(score))