import sys

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    candies = list(map(int, sys.stdin.readline().strip().split()))
    dic = {1:0, 2:0}
    for candy in candies:
        dic[candy] += 1
    if (n % 2 == 0 and dic[2] % 2 == 0 and dic[1] % 2 == 0) or (dic[1] % 2 == 0 and dic[1] != 0):
        print("YES")
    else:
        print("NO")