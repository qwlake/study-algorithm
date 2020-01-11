from math import gcd
import sys

def lcm(x,y):
    w = gcd(x,y)
    q = x*y//gcd(x,y)
    print(w, q)
    return q

N = int(input())
a = sorted(list(map(int, sys.stdin.readline().split())))
print(a)
m = 0
for i in range(N-1):
    for j in range(i+1, N):
        ret = lcm(a[i],a[j])
        if ret > m:
            m = ret
print(m)