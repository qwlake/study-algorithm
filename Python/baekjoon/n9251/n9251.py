s1, s2 = ' '+input(), ' '+input()
dp = [[0] * (len(s2)) for _ in range(len(s1))]
for i in range(1, len(dp)):
    for j in range(1, len(dp[0])):
        if s1[i] == s2[j]:
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
print(dp[-1][-1])