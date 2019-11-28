import sys

# a = [list(sys.stdin.readline())[:-1] if i < 9 else list(sys.stdin.readline()) for i in range(10)]
a = [sys.stdin.readline()[:-1] if i < 9 else sys.stdin.readline() for i in range(10)]
print(a)

def count(i, j, r, c, n):
    

# 1 2 3
# 4 x 5
# 6 7 8
def direction(i, j):
    count(i, j, 0, 1, 1)
    count(i, j, 1, 1, 1)
    count(i, j, 1, 0, 1)
    count(i, j, 1, -1, 1)


for i in range(10):
    for j in range(10):
        if a[i][j] == "1":
            direction(i, j, 1)
            break