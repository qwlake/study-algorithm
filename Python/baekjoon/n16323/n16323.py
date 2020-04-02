import sys

n, s = map(int, sys.stdin.readline().split())
arr = list()
for _ in range(n):
    name, b = map(str, sys.stdin.readline().split())
    arr.append((name, int(b)))
arr.sort(key=lambda x: -x[1])
ret = list()
for name, b in arr:
    if b <= s:
        s -= b
        ret.append(name)
    if s <= 0:
        break
if s == 0:
    print(len(ret))
    for r in ret:
        print(r)
else:
    print(0)