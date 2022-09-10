import sys
input = sys.stdin.readline


def solution():
    code = list(map(int, input().strip()))
    dp = [0] * (len(code) + 1)
    if code[0] == 0:
        print("0")
        return
    code.insert(0, 0)
    dp[0] = dp[1] = 1
    for i in range(2, len(code)):
        if code[i] > 0:
            dp[i] += dp[i - 1]
        if 10 <= code[i - 1] * 10 + code[i] <= 26:
            dp[i] += dp[i - 2]
    print(dp[-1] % 1000000)


if __name__ == '__main__':
    solution()
