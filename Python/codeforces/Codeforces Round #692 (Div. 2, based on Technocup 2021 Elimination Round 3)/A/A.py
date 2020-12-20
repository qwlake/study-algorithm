import sys

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    a = sys.stdin.readline().strip()
    for i in range(len(a)):
        if a[len(a)-i-1] != ')':
            i -= 1
            break
    if i+1 <= len(a)-i-1:
        print("NO")
    else:
        print("YES")