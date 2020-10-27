import sys
sys.setrecursionlimit(10000)

directions = (
    (-1, 0),
    (0, -1),
    (1, 0),
    (0, 1)
)

def dfs(maze, dp, r, c, destination_r, destination_c):
    ret = []
    if r == destination_r and c == destination_c:
        return 1
    for direction in directions:
        if maze[r+direction[0]][c+direction[1]] < maze[r][c]:
            if dp[r+direction[0]][c+direction[1]] > 0:
                ret.append(dp[r+direction[0]][c+direction[1]])
            elif dp[r+direction[0]][c+direction[1]] == 0:
                res = dfs(maze, dp, r+direction[0], c+direction[1], destination_r, destination_c)
                ret.append(res)
    if ret:
        dp[r][c] += sum(ret)
        return dp[r][c]
    else:
        dp[r][c] = -1
        return 0

r, c = map(int, sys.stdin.readline().split())
maze = [list(map(int, f'10001 {sys.stdin.readline()} 10001'.split())) for _ in range(r)]
maze.insert(0, [10001]*(c+2))
maze.append([10001]*(c+2))

dp = [[0]*(c+2) for _ in range(r+2)]
dfs(maze, dp, 1, 1, r, c)
print(dp[1][1])
