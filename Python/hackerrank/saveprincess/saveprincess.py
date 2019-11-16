
def displayPathtoPrincess(n,grid):
    m, p = list(), list()
    for i in range(n):
        for j in range(n):
            if grid[i][j] == "m":
                m = [i,j]
            elif grid[i][j] == "p":
                p = [i,j]
    while p[0] != m[0]:
        if p[0]-m[0] > 0:
            p[0] -= 1
            print("DOWN")
        else:
            p[0] += 1
            print("UP")
    while p[1] != m[1]:
        if p[1]-m[1] > 0:
            p[1] -= 1
            print("RIGHT")
        else:
            p[1] += 1
            print("LEFT")


m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)