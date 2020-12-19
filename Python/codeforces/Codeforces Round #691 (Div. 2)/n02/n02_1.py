import sys

n = int(sys.stdin.readline())
maze = [[0]*1001 for _ in range(1001)]
dirs = ((1,0),(0,1),(-1,0),(0,-1))
count = 0

def loop(x, y, cnt, pre):
    global maze, count
    if cnt == n:
        if maze[x][y] == 0:
            count += 1
            maze[x][y] = 1
        return
    if pre % 2 == 0:
        nxt_dir = 1
    else:
        nxt_dir = 0
    for i in range(4):
        nxt_x, nxt_y = x + dirs[i][0], y + dirs[i][1]
        if nxt_x < 0 or nxt_y < 0 or i % 2 == pre:
            continue
        loop(nxt_x, nxt_y, cnt+1, i % 2)

loop(0, 1, 1, 1)
loop(1, 0, 1, 0)
tmp = 0
for i in range(1001):
    if maze[0][i] == 1:
        tmp += 1
    if maze[i][0] == 1:
        tmp += 1
print((count - tmp) * 4 + tmp * 2)