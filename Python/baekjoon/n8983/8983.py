import sys
import bisect
input1 = sys.stdin.readline


def main():
    m, n, l = map(int, input1().split())
    seat = sorted(list(map(int, input1().split())))
    cnt = 0
    for _ in range(n):
        x, y = map(int, input1().split())
        if y > l:
            continue
        idx = bisect.bisect_left(seat, x)
        if idx >= len(seat):
            target = (idx - 1,)
        elif idx == 0:
            target = (0,)
        else:
            target = (idx - 1, idx)
        a = l - y
        for t in target:
            if abs(seat[t] - x) <= a:
                cnt += 1
                break

    return cnt


if __name__ == "__main__":
    print(main())
