stack = []
p, f, g_size = [], [], []
grid = []

def packman(p_r, p_c):
    stack.append((p_r, p_c))
    grid[p_r][p_c] = "*"
    if p_r == f[0] and p_c == f[1]:
        print(len(stack))
        for s in stack:
            print("{} {}".format(s[0], s[1]))
    if (grid[p_r-1][p_c] == "-" or grid[p_r-1][p_c] == ".") and 0 <= p_r-1:
        packman(p_r-1, p_c)
        stack.pop()
    if (grid[p_r][p_c-1] == "-" or grid[p_r][p_c-1] == ".") and 0 <= p_c-1:
        packman(p_r, p_c-1)
        stack.pop()
    if (grid[p_r][p_c+1] == "-" or grid[p_r][p_c+1] == ".") and p_c+1 < g_size[1]:
        packman(p_r, p_c+1)
        stack.pop()
    if (grid[p_r+1][p_c] == "-" or grid[p_r+1][p_c] == ".") and p_r+1 < g_size[0]:
        packman(p_r+1, p_c)
        stack.pop()

p = list(map(int, input().split(" ")))
f = list(map(int, input().split(" ")))
g_size = list(map(int, input().split(" ")))

for i in range(0, g_size[0]): 
    grid.append(list(input()))

packman(p[0], p[1])

