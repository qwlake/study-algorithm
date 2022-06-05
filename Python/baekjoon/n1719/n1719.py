import sys
input = sys.stdin.readline


def solution():
    n, m = map(int, input().split())
    arr = [[200001] * n for _ in range(n)]
    ans = [['-'] * n for _ in range(n)]
    for _ in range(m):
        x, y, c = map(int, input().split())
        arr[x - 1][y - 1] = arr[y - 1][x - 1] = c
        ans[x - 1][y - 1] = str(y)
        ans[y - 1][x - 1] = str(x)

    for k in range(n):
        for i in range(n):
            if i == k:
                continue
            for j in range(i + 1, n):
                t = arr[i][k] + arr[k][j]
                if arr[i][j] > t:
                    arr[i][j] = arr[j][i] = t
                    ans[i][j] = ans[i][k]
                    ans[j][i] = ans[j][k]

    print('\n'.join(map(' '.join, ans)))


if __name__ == '__main__':
    solution()
