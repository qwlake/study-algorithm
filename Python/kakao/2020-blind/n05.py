from typing import List

def build(st:List[List[int]], frame:List[int]):
    r = frame[0]
    c = frame[1]
    s = frame[2] # 0 기둥, 1 보
    
    if s == 0:
        if c == 0 or st[r][c-1] != -1 or (r > 0 and st[r-1][c] == 1):
            st[r][c] = s
    elif s == 1:
        if st[r][c-1] == 0: # 기둥 있는지
            st[r][c] = s
        elif (r-1 >= 0 and st[r-1][c] == 1) and (r+1 < len(st) and st[r+1][c] == 1): # 중간. 보,보
            st[r][c] = s
        elif r < len(st)-1 and st[r+1][c-1] == 0: # 중간. 기둥
            st[r][c] = s

def delete(st:List[List[int]], frame:List[int]):
    r = frame[0]
    c = frame[1]
    s = frame[2] # 0 기둥, 1 보
    
    if st[r][c] == -1:
        return
    
    if s == 0:
        if st[r-1][c+1] == 1:
            if not (st[r-1][c] == 0 or (st[r-2][c+1] == 1 and st[r][c+1] == 1)):
                return
        if st[r+1][c] == 1:
            if not (st[r+1][c] == 0 or (st[r+1][c+1] == 1 and st[r-1][c+1] == 1)):
                return
        if st[r][c+1] == 0:
            if not (st[r-1][c+1] == 1 or st[r+1][c] == 1):
                return
    else:
        if st[r-1][c] == 1:
            if not (st[r-1][c-1] == 0 or st[r][-1] == 0):
                return
        if st[r+1][c] == 1:
            if not (st[r+1][c-1] == 0 or st[r+2][c-1] == 0):
                return
        if st[r][c] == 


def solution(n, build_frame):
    answer = []

    st = [[-1 for _ in range(n+1)] for _ in range(n+1)]
    # [
    #     [-1, -1, -1, -1, -1], 
    #     [-1, -1, -1, -1, -1], 
    #     [-1, -1, -1, -1, -1], 
    #     [-1, -1, -1, -1, -1], 
    #     [-1, -1, -1, -1, -1]
    # ]

    for frame in build_frame:
        if frame[3] == 1:
            build(st, frame)
        else:
            delete(st, frame)

    for i in range(len(st)):
        for j in range(len(st)):
            if st[i][j] != -1:
                answer.append([i, j, st[i][j]])

    return answer

a = solution(
    5,
    [
        [1,0,0,1],
        [1,1,1,1],
        [2,1,0,1],
        [2,2,1,1],
        [5,0,0,1],
        [5,1,0,1],
        [4,2,1,1],
        [3,2,1,1]
    ]
) # [[1,0,0],[1,1,1],[2,1,0],[2,2,1],[3,2,1],[4,2,1],[5,0,0],[5,1,0]]
print(a)

a = solution(
    5,
    [
        [0,0,0,1],
        [2,0,0,1],
        [4,0,0,1],
        [0,1,1,1],
        [1,1,1,1],
        [2,1,1,1],
        [3,1,1,1],
        [2,0,0,0],
        [1,1,1,0],
        [2,2,0,1]
    ]
) # [[0,0,0],[0,1,1],[1,1,1],[2,1,1],[3,1,1],[4,0,0]]
print(a)