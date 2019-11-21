import sys
N = int(input())
a = [int(sys.stdin.readline()) for i in range(N)]
a.insert(0, 0)
sets = set()
for i in range(1, N+1):
    stack = [i]
    tmp = []
    while len(stack) != 0:
        p = stack.pop()
        tmp.append(p)
        stck_size = len(stack)
        if a[i] == p:
            sets.update(set(tmp))
            break
        for j in range(1, N+1):
            if a[j] == p:
                stack.append(j)
        if stck_size == len(stack):
            tmp.pop()
sets = sorted(list(sets))
print(len(sets))
for e in sets:
    print(e)
