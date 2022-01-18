from sys import stdin


_a, _b, _c = (0, 1), (1, 1), (1, 0)
next_step = (
    ((_a,), (_b, _a, _c)),  # 우
    ((_a,), (_b, _a, _c), (_c,)),  # 대각
    ((_b, _a, _c), (_c,)),  # 하
)
next_direction = (
    (0, 1),
    (0, 1, 2),
    (1, 2),
)


def is_possible(arr, x, y):
    n = len(arr)
    return 0 <= x < n and 0 <= y < n and arr[x][y][3] >= 0


def can_move_2(arr, pipe, steps):
    for a, b in steps:
        x, y = pipe[0] + a, pipe[1] + b
        if not is_possible(arr, x, y):
            return False
    return True


def can_move(arr, pipe, direction):
    candidates = []
    for i, steps in enumerate(next_step[direction]):
        if can_move_2(arr, pipe, steps):
            a, b = steps[0]
            x, y = pipe[0] + a, pipe[1] + b
            candidates.append((x, y, next_direction[direction][i]))
    return candidates


def loop(arr, pipe, direction):
    if pipe[0] == pipe[1] == len(arr) - 1:
        return 1
    candidates = can_move(arr, pipe, direction)
    cnt = 0
    for x, y, d in candidates:
        if arr[x][y][d] == 0:
            result = loop(arr, [x, y], d)
            if result > 0:
                arr[x][y][d] = result
            else:
                arr[x][y][d] = -1
        cnt += max(arr[x][y][d], 0)
    return cnt


def main():
    n = int(stdin.readline())
    arr = [list(map(lambda x: [-int(x)] * 4, stdin.readline().split())) for _ in range(n)]
    pipe = [0, 1]
    direction = 0
    result = loop(arr, pipe, direction)
    return result


if __name__ == "__main__":
    print(main())
