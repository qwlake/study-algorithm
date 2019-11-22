import sys
a = [[0]+list(map(int, sys.stdin.readline().split())) for i in range(4)]
total = 0
mat = [[0 for _ in range(101)] for _ in range(101)]
for r in a:
    for i in range(r[1], r[3]):
        for j in range(r[2], r[4]):
            if mat[i][j] == 0:
                total += 1
                mat[i][j] = 1
    for i in range(10):
        print(mat[i][:10])
    print()
print(total)