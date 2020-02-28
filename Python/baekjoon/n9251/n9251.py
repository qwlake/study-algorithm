s1, s2 = ' '+input(), ' '+input()
dp = [[0 for _ in range(len(s2))] for _ in range(len(s1))]
m, x, y = 0, 0, 0
for i in range(1, len(dp)):
    for j in range(1, len(dp[0])):
        if s1[i] == s2[j]:
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        if m < dp[i][j]:
            m = dp[i][j]
            x, y = i, j
def find_answer(nxt, x, y):
    for i in range(x, 0, -1):
        for j in range(y, 0, -1):
            if dp[i][j] == nxt:
                return s1[i], s2[j]
    return 0,0
nxt = m
s1_ans, s2_ans = [s1[x]], [s2[y]]
while nxt > 1:
    nxt, x, y = nxt-1, x-1, y-1
    s1_a, s2_a = find_answer(nxt, x, y)
    s1_ans.append(s1_a)
    s2_ans.append(s2_a)
print(m)