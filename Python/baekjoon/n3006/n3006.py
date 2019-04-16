import sys

N = int(sys.stdin.readline())
read = [int(sys.stdin.readline())-1 for i in range(N)]
result = []

for i in range(int(N/2)):
    idx = read.index(i)
    result.append(abs(idx-i))
    read.insert(i, read.pop(idx))

    idx = read.index(N-i-1)
    result.append(abs(idx - (N-i-1)))
    read.insert(N-i-1, read.pop(idx))

if N/2 != 0:
    result.append(0)

for i in result:
    print(i)