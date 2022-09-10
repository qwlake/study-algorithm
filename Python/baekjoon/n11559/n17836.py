import sys
from collections import deque

input = sys.stdin.readline

DELTA = (1, 0), (0, 1), (-1, 0), (0, -1)


def is_in_range(n, m, x, y):
    return 0 <= x < n and 0 <= y < m


def bfs(puyo, offset, visit, j, i, p, seq):
    oj = j - offset[i]
    stack = [(j, i)]
    q = deque([[(oj, i)]])
    while q:
        nexts = []
        for r, c in q.popleft():
            for i in range(4):
                x, y = DELTA[i][0] + r, DELTA[i][0] + c
                if not is_in_range(24, 6, x, y):
                    continue
                if puyo[x][y] == p and visit[x + offset[y]][y] != seq:
                    visit[x][y] = seq
                    stack.append((x + offset[y], y))
                    nexts.append((x, y))
        if nexts:
            q.append(nexts)
    return stack


def mark(puyo, stack, offset):
    if len(stack) < 4:
        return
    for r, c in stack:
        puyo[r][c] = '.'
        offset[c] += 1


def solution():
    puyo = [['.'] * 6 for _ in range(12)] + [list(input()) for _ in range(12)]
    visit = [[0] * 6 for _ in range(12)]
    offset = [0] * 6
    seq = 1
    while True:
        stack = []
        for i in range(6):
            for j in range(23, -1, -1):
                oj = j - offset[i]
                if puyo[oj][i] != '.':
                    visit[j][i] = seq
                    result = bfs(puyo, offset, visit, j, i, puyo[oj][i], seq)
                    if len(result) >= 4:
                        stack += result
                    seq += 1
                    mark(puyo, stack, offset)



if __name__ == '__main__':
    solution()
