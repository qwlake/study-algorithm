INF = 1000000000

# A[i], B[i]: 그룹의 i번 정점과 매칭된 상대편 그룹 정점 번호
temp = input().split(" ")
N = int(temp[0])
W = int(temp[1])
A = [-1 for _ in range(N)]
B = [-1 for _ in range(W)]
dist = [0 for _ in range(N)] # dist[i]: (A그룹의) i번 정점의 레벨(?)
used = [False for _ in range(N)] # used: (A그룹의) 이 정점이 매칭에 속해 있는가?
adj = [[] for _ in range(N)]

# 호프크로프트 카프 전용 bfs 함수: A그룹의 각 정점에 레벨을 매김
Q = []
def bfs():
    # 매칭에 안 속한 A그룹의 정점만 레벨 0인 채로 시작
    for i in range(N):
        if not used[i]:
            dist[i] = 0
            Q.append(i)
        else:
            dist[i] = INF
    # BFS를 통해 A그룹 정점에 0, 1, 2, 3, ... 의 레벨을 매김
    while len(Q) != 0:
        a = Q.pop(0)
        for b in adj[a]:
            if B[b] != -1 and dist[B[b]] == INF:
                dist[B[b]] = dist[a] + 1
                Q.append(B[b])
                
# 호프크로프트 카프 전용 dfs 함수: 새 매칭을 찾으면 true
def dfs(a):
    for b in adj[a]:
        # 이분 매칭 코드와 상당히 유사하나, dist 배열에 대한 조건이 추가로 붙음
        if B[b] == -1 or dist[B[b]] == dist[a]+1 and dfs(B[b]):
            # used 배열 값도 true가 됨
            used[a] = True
            A[a] = b
            B[b] = a
            return True
    return False

from sys import stdin

if __name__ == "__main__":
    # 그래프 정보 입력받기
    for i in range(N):
        temp = stdin.readline().split(" ")
        J = int(temp[0])
        for j in range(1, J+1):
            adj[i].append(int(temp[j])-1)

    # 호프크로프트 카프 알고리즘
    match = 0
    while True:
        # 각 정점에 레벨을 매기고 시작
        bfs()

        # 이분 매칭과 비슷하게 A그룹 정점을 순회하며 매칭 증가량 찾음
        flow = 0
        for i in range(N):
            if not used[i] and dfs(i):
                flow += 1

        # 더 이상 증가 경로를 못 찾으면 알고리즘 종료
        if flow == 0:
            break
        # 찾았을 경우 반복
        match += flow

    # 결과 출력
    print(match);