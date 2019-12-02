import sys

n = int(input())
a = {i:0 for i in range(1,n+1)}

while True:
    t = list(map(int, sys.stdin.readline().split()))
    if t[0] == -1:
        break
    a[t[0]] += 1
    a[t[1]] += 1

sort = sorted(a.items(), key=lambda x: x[1], reverse=True)
score = n-sort[0][1]
count = 0
can = ""
for i, e in enumerate(sort):
    if e[1] != sort[0][1]:
        count = i
        break
    else:
        can += str(e[0]) + " "
print(score, count)
print(can.strip())
