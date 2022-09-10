import sys
from collections import deque

input = sys.stdin.readline

DELTA = (1, 0), (0, 1), (-1, 0), (0, -1)


def is_in_range(n, m, x, y):
    return 0 <= x < n and 0 <= y < m


class Gram:
    def __init__(self, cnt, r, c):
        self.cnt, self.r, self.c = cnt, r, c


class Status:
    def __init__(self, n, m, maze):
        self.n, self.m = n, m
        self.maze = maze
        self.gram = None
        self.cnt = 0

    def get_gram_dist(self):
        if self.gram is None:
            return 100000001
        else:
            return self.gram.cnt + (self.n - 1 - self.gram.r) + (self.m - 1 - self.gram.c)


def bfs(status):
    n, m, maze = status.n, status.m, status.maze
    hit = ('0', '2')
    maze[0][0] = '9'
    q = deque([[(0, 0)]])
    while q:
        status.cnt += 1
        popped = q.popleft()
        nxts = []
        for r, c in popped:
            for i in range(4):
                a, b = DELTA[i][0], DELTA[i][1]
                x, y = r + a, c + b
                if not is_in_range(n, m, x, y):
                    continue
                if maze[x][y] in hit:
                    if x == n - 1 and y == m - 1:
                        return True
                    if maze[x][y] == '2':
                        status.gram = Gram(status.cnt, x, y)
                    maze[x][y] = '9'
                    nxts.append((x, y))
        if nxts:
            q.append(nxts)
    status.cnt = 100000001
    return False or status.gram


def solution():
    n, m, t = map(int, input().split())
    maze = [input().split() for _ in range(n)]

    status = Status(n, m, maze)
    result = bfs(status)

    if result is False:
        print("Fail")
    else:
        dist = min(status.cnt, status.get_gram_dist())
        if dist <= t:
            print(dist)
        else:
            print("Fail")


if __name__ == '__main__':
    solution()
