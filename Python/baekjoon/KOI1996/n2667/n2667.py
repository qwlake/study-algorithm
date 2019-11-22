import sys

N = int(input())
def bfs(a, r, c):
    cnt = 0
    nxt = [[r,c]]
    a[r][c] = "0"
    while len(nxt) != 0:
        cnt += 1
        p = nxt.pop(0)
        i, j = p[0], p[1]
        if i-1 >= 0 and a[i-1][j] == "1":
            a[i-1][j] = "0"
            nxt.append([i-1, j])
        if i+1 < N and a[i+1][j] == "1":
            a[i+1][j] = "0"
            nxt.append([i+1, j])
        if j-1 >= 0 and a[i][j-1] == "1":
            a[i][j-1] = "0"
            nxt.append([i, j-1])
        if j+1 < N and a[i][j+1] == "1":
            a[i][j+1] = "0"
            nxt.append([i, j+1])
    return cnt

a = [list(sys.stdin.readline())[:-1] if i < N-1 else list(sys.stdin.readline()) for i in range(N)]
homes_list = []
for i in range(len(a)):
    for j in range(len(a[0])):
        if a[i][j] == "1":
            homes_list.append(bfs(a, i, j))
homes_list = sorted(homes_list)
print(len(homes_list))
for h in homes_list:
    print(h)