import sys
In = sys.stdin.readline
N = int(In())

def bfs(N):
    que = [1]
    cnt = 0
    cnt_dic = {1:0}
    visited = [False for _ in range(1000001)]
    while True:
        q = que.pop(0)
        cnt = cnt_dic[q] + 1
        temp = (q*3, q*2, q+1)
        if visited[N]:
            return cnt_dic[N]
        for i in range(3):
            if temp[i] <= N and not visited[temp[i]]:
                cnt_dic[temp[i]] = cnt 
                visited[temp[i]] = True
                que.append(temp[i])
# print(bfs(N))

def dp(N):
    cnt_list = [0 for i in range(N+1)]
    for i in range(2, N+1):
        cnt_list[i] = cnt_list[i-1] + 1
        if i % 2 == 0:
            cnt_list[i] = min(cnt_list[i], cnt_list[int(i//2)]+1)
        if i % 3 == 0:
            cnt_list[i] = min(cnt_list[i], cnt_list[int(i//3)]+1)
    return cnt_list[N]
print(dp(N))
