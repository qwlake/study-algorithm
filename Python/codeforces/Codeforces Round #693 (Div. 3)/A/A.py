import sys

for _ in range(int(sys.stdin.readline())):
    w, h, n = map(int, sys.stdin.readline().strip().split())
    cnt = 1
    while w > 1 and w % 2 == 0:
        w //= 2
        cnt *= 2
    while h > 1 and h % 2 == 0:
        h //= 2
        cnt *= 2
    if cnt >= n:
        print("YES")
    else:
        print("NO")
    