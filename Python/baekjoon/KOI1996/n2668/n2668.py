import sys
N = int(input())
a = [int(sys.stdin.readline()) for i in range(N)]
a.insert(0, 0)
sets = set()
for i in range(1, N+1):
    stack = [(i, [i])]
    while len(stack) != 0:
        s, s_list = stack.pop()
        if a[i] == s:
            sets.update(set(s_list))
            break
        for j in range(1, N+1):
            if a[j] == s:
                stack.append((j, s_list+[j]))
sets = sorted(list(sets))
print(len(sets))
for e in sets:
    print(e)
