import sys
input = sys.stdin.readline


def solution():
    n, k = map(int, input().split())
    point = [list(map(int, input().split())) for _ in range(n)]

    dist = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1):
            dist[i][j] = abs(point[i][0] - point[j][0]) + abs(point[i][1] - point[j][1])
            dist[j][i] = abs(point[i][0] - point[j][0]) + abs(point[i][1] - point[j][1])

    dp = [[4000] * n for _ in range(k + 1)]
    dp[0][0] = 0

    # k = 0
    for i in range(1, n):
        dp[0][i] = dp[0][i - 1] + dist[i - 1][i]

    # k = 1, 2, ... k
    for i in range(1, k + 1):
        dp[i][0] = 0
        dp[i][1] = dp[i - 1][1]
        dp[i][i] = dist[0][i]
        for j in range(1, n):
            for m in range(i, 0, -1):
                if j - m - 1 < 0:
                    continue
                dp[i][j] = min(dp[i][j], dp[i - m][j - m - 1] + dist[j][j - m - 1], dp[i][j - 1] + dist[j - 1][j])

    print(dp[-1][-1])


if __name__ == '__main__':
    solution()
