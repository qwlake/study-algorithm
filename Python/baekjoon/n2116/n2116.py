import sys
input = sys.stdin.readline


get_side_indices = {
    0: [1, 2, 3, 4],
    1: [0, 2, 4, 5],
    2: [0, 1, 3, 5],
    3: [0, 2, 4, 5],
    4: [0, 1, 3, 5],
    5: [1, 2, 3, 4]
}


get_top_indices = {
    0: 5,
    1: 3,
    2: 4,
    3: 1,
    4: 2,
    5: 0,
}


def solution():
    n = int(input())
    d = [list(map(int, input().split())) for _ in range(n)]

    result = 0
    for i in range(6):
        top_idx = get_top_indices[i]
        top_num = d[0][top_idx]
        side_indices = get_side_indices[i]

        # 첫 번째 주사위 옆면 최대값 -> tmp
        tmp = -1
        for j in side_indices:
            tmp = max(d[0][j], tmp)

        # 두 번째 주사위부터 옆 면이 최대값인 것을 tmp 저장
        for j in range(1, len(d)):
            bottom_idx = d[j].index(top_num)
            top_idx = get_top_indices[bottom_idx]
            top_num = d[j][top_idx]
            side_indices = get_side_indices[bottom_idx]
            tmp2 = -1
            for k in side_indices:
                tmp2 = max(tmp2, d[j][k])
            tmp += tmp2

        result = max(result, tmp)

    print(result)


if __name__ == '__main__':
    solution()
