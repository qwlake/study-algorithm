import sys
n = int(input())
a = [sorted(list(map(int, sys.stdin.readline().split(" ")))) for _ in range(n)]
a = sorted(a, key=lambda x:(x[0], x[1]))
d = [0]*n
for i, e in enumerate(a):
    d[i] = 1
    for j in range(i):
        if e[1] >= a[j][1]:
            d[i] = max(d[j]+1, d[i])
print(max(d))
print(a)