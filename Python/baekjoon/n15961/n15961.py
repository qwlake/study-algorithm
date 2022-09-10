import sys
from collections import defaultdict

input = sys.stdin.readline


def solution():
    n, d, k, c = map(int, input().split())
    plates = [int(input())for _ in range(n)]

    keep = defaultdict(int)
    coupon_cnt = 0
    for i in range(-k + 1, 1):
        keep[plates[i]] += 1
        if plates[i] == c:
            coupon_cnt += 1
    max1 = len(keep)
    max2 = 0
    for i in range(1, n):
        keep[plates[i]] += 1
        keep[plates[i - k]] -= 1
        if plates[i] == c:
            coupon_cnt += 1
        if plates[i - k] == c:
            coupon_cnt -= 1
        if keep[plates[i - k]] == 0:
            del keep[plates[i - k]]
        if max1 == len(keep):
            max2 = max(len(keep.keys()) + int(not bool(coupon_cnt)), max2)
        elif max1 < len(keep):
            max2 = len(keep.keys()) + int(not bool(coupon_cnt))
            max1 = len(keep)
    print(max2)


if __name__ == '__main__':
    solution()
