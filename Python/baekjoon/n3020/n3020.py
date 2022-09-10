import sys
input = sys.stdin.readline


def solution():
    n, h = map(int, input().split())
    walls = [[0] * 2 for _ in range(h)]
    for i in range(n):
        w = int(input())
        if i % 2 == 0:
            walls[0][0] += 1
            walls[w - 1][1] += 1
        else:
            walls[-w][0] += 1
            walls[-1][1] += 1

    current = walls[0][0]
    m, m_cnt = walls[0][0], 1
    for i in range(1, len(walls)):
        current += walls[i][0] - walls[i - 1][1]
        if m == current:
            m_cnt += 1
        elif m > current:
            m, m_cnt = current, 1

    print(m, m_cnt)


if __name__ == '__main__':
    solution()
