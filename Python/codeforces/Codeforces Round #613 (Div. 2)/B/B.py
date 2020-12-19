import sys
total = int(input())
for _ in range(total):
    N = int(input())
    a = list(map(int, sys.stdin.readline().split()))
    flag = True
    for e in a:
        if e <= 0:
            print("NO")
            flag = False
            break
    if flag:
        print("YES")