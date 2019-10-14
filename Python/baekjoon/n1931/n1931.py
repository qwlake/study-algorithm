import sys
In = sys.stdin.readline

N = int(In())
c_list = [(*map(int, In().split()),) for _ in range(N)]
c_list = sorted(c_list, key=lambda c: (c[1], c[0]))
idx = 0
cnt = 0
for c in c_list:
    if idx <= c[0]:
        idx = c[1]
        cnt += 1
print(cnt)