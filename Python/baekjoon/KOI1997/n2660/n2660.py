import sys

n = int(input())
a = [[0 for _ in range(n+1)] for _ in range(n+1)]

while True:
    t = list(map(int, sys.stdin.readline().split()))
    if t[0] == -1:
        break
    a[t[0]][t[1]] = 1
    a[t[1]][t[0]] = 1

def find(idx):
    s = {idx}
    q = [(idx, 0)]
    m = 0
    while len(q) != 0:
        p, d = q.pop(0)
        m = d
        for i, e in enumerate(a[p]):
            if e == 1 and i not in s:
                q.append((i, d+1))
                s.add(i)
    return m

score_dic = dict()
for i in range(1,n+1):
    score_dic[i] = find(i)
sort = sorted(score_dic.items(), key=lambda x: x[1])
count = n
can = ""
for i, e in enumerate(sort):
    if e[1] != sort[0][1]:
        count = i
        break
    else:
        can += str(e[0]) + " "
print(sort[0][1], count)
print(can.strip())