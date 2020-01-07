import sys
N = int(input())
a = ["X"+sys.stdin.readline().split()[0] for _ in range(N)]
a.insert(0, "X"*N)
mola = "MOLA"
dp = [[["", 0] for _ in range(N+1)] for _ in range(N+1)]
for i in range(1,N+1):
    for j in range(1,N+1):
        t1, t2 = dp[i][j-1], dp[i-1][j]
        s1 = t1[0] + a[i][j]
        s2 = t2[0] + a[i][j]
        t1_cnt, t2_cnt = t1[1], t2[1]
        idx1 = "MOLA".find(s1)
        idx2 = "MOLA".find(s2)
        if s1 == "MOLA":
            t1_cnt = t1_cnt + 1
            s1 = ""
        if s2 == "MOLA":
            t2_cnt = t2_cnt + 1
            s2 = ""
        if idx1 is not 0:
            s1 = ""
            if a[i][j] == 'M':
                s1 = "M"
        if idx2 is not 0:
            s2 = ""
            if a[i][j] == 'M':
                s2 = "M"
        if t1_cnt < t2_cnt:
            dp[i][j] = [s2, t2_cnt]
        elif t1_cnt > t2_cnt:
            dp[i][j] = [s1, t1_cnt]
        else:
            dp[i][j] = [s2, t2_cnt] if len(s1) < len(s2) else [s1, t1_cnt]
print(dp[N][N][1])