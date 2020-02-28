s1_len = int(input())
s1 = ' '+input()
s2_len = int(input())
s2 = ' '+input()
dp = [[0 for _ in range(len(s2))] for _ in range(len(s1))]
m, x, y = 0, 0, 0
idx_set = set()
for i in range(1, len(dp)):
    for j in range(1, len(dp[0])):
        if s1[i] == s2[j]:
            dp[i][j] = dp[i-1][j-1]+3
            dp[i][j] = dp[i][j] if dp[i][j]>=3 else 3
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])-2
            dp[i][j] = dp[i][j] if dp[i][j]>=-2 else -2
        if m < dp[i][j]:
            m = dp[i][j]
            x, y = i, j
s1_ans, s2_ans = [s1[x]], [s2[y]]
for p in dp:
    print(p)
while x-1 > 0 and y-1 > 0:
    if dp[x-1][y-1] > 0:
        s1_ans.append(s1[x-1])
        s2_ans.append(s2[y-1])
        x, y = x-1, y-1
    elif dp[x][y-1] > 0:
        s2_ans.append(s1[x])
        y = y-1
    elif dp[x-1][y] > 0:
        s1_ans.append(s2[y])
        x = x-1
    else:
        break
s1_ans.reverse(), s2_ans.reverse()
print(m)
print(''.join(s1_ans))
print(''.join(s2_ans))