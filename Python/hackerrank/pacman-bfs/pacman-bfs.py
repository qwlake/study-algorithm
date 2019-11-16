full_path = []
queue = []
grid = []

p = list(map(int, input().split(" ")))
f = list(map(int, input().split(" ")))
g_size = list(map(int, input().split(" ")))

for i in range(0, g_size[0]): 
    grid.append(list(input()))

grid[p[0]][p[1]] = "*"
queue.append((p[0], p[1], ["{} {}".format(p[0], p[1])]))
while len(queue) != 0:
    info = queue.pop(0)
    full_path.append((info[0], info[1]))
    grid[info[0]][info[1]] = "*"
    if info[0] == f[0] and info[1] == f[1]:
        print(len(full_path))
        for p in full_path:
            print("{} {}".format(p[0], p[1]))
        print(len(info[2])-1)
        for p in info[2]:
            print(p)
        break

    if (grid[info[0]-1][info[1]] == "-" or grid[info[0]-1][info[1]] == ".") and 0 <= info[0]-1:
        temp = info[2].copy()
        temp.append("{} {}".format(info[0]-1, info[1]))
        grid[info[0]-1][info[1]] = "*"
        queue.append((info[0]-1, info[1], temp))

    if (grid[info[0]][info[1]-1] == "-" or grid[info[0]][info[1]-1] == ".") and 0 <= info[1]-1:
        temp = info[2].copy()
        temp.append("{} {}".format(info[0], info[1]-1))
        grid[info[0]][info[1]-1] = "*"
        queue.append((info[0], info[1]-1, temp))

    if (grid[info[0]][info[1]+1] == "-" or grid[info[0]][info[1]+1] == ".") and info[1]+1 < g_size[1]:
        temp = info[2].copy()
        temp.append("{} {}".format(info[0], info[1]+1))
        grid[info[0]][info[1]+1] = "*"
        queue.append((info[0], info[1]+1, temp))

    if (grid[info[0]+1][info[1]] == "-" or grid[info[0]+1][info[1]] == ".") and info[0]+1 < g_size[0]:
        temp = info[2].copy()
        temp.append("{} {}".format(info[0]+1, info[1]))
        grid[info[0]+1][info[1]] = "*"
        queue.append((info[0]+1, info[1], temp))
