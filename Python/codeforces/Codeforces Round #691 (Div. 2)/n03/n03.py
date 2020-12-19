import sys
from math import gcd

an, bn = map(int, sys.stdin.readline().strip().split())
a = list(map(int, sys.stdin.readline().strip().split()))
b = list(map(int, sys.stdin.readline().strip().split()))
print(a, b)

tmp = []
for i in range(bn):
    lst = []
    for j in range(an):
        lst.append(a[j] + b[i])
    tmp.append(gcd(*lst))
print(' '.join(tmp))