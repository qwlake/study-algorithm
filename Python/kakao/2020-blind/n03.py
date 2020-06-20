from typing import List, Tuple

def copy2d(arr):
    return [a.copy() for a in arr]

def rotate(arr:List[List[int]]) -> List[List[int]]:
    ret = [[0 for _ in range(len(arr))] for _ in range(len(arr))]
    for i in range(len(arr)):
        for j in range(len(arr)):
            ret[j][len(arr)-i-1] = arr[i][j]
    return ret

def check(arr1:List[List[int]], arr2:List[List[int]], x:int, y:int) -> bool:
    s = int(len(arr1)/3)
    e = int(len(arr1)/3*2)
    arr = copy2d(arr1)
    for i in range(len(arr2)):
        for j in range(len(arr2)):
            arr[x+i][y+j] += arr2[i][j]
    for i in range(s,e):
        for j in range(s,e):
            if arr[i][j] != 1:
                return False
    return True

def solution(key, lock):
    extended = [[0 for _ in range(len(lock)*3)] for _ in range(len(lock)*3)]
    for i in range(len(lock)):
        for j in range(len(lock)):
            extended[i+len(lock)][j+len(lock)] = lock[i][j]
    
    for _ in range(4):
        key = rotate(key)
        for i in range(len(lock)*2):
            for j in range(len(lock)*2):
                if check(extended, key, i, j):
                    return True

    return False

a = solution(
    [[0, 0], [0, 0]], 
    [[1, 1], [1, 0]]
) # True
print(a)

a = solution(
    [[0, 0, 0], [1, 0, 0], [0, 1, 1]], 
    [[1, 1, 1], [1, 1, 0], [1, 0, 1]]	
) # True
print(a)
