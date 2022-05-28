
def solution():
    n, m = map(int, input().split())
    arr = [[[100001, -1] for _ in range(n)] for _ in range(n)]
    for _ in range(m):
        x, y, c = map(int, input().split())
        arr[x - 1][y - 1] = [c, y - 1]
        arr[y - 1][x - 1] = [c, x - 1]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                t = arr[i][k][0] + arr[k][j][0]
                if arr[i][j][0] > t:
                    arr[i][j] = [t, arr[i][k][1]]

    result = ''
    for i in range(n):
        for j in range(n):
            if i == j:
                result += '- '
            else:
                result += str(arr[i][j][1] + 1) + ' '
        result += '\n'
    print(result)


if __name__ == '__main__':
    solution()
