import sys

n = int(input())
a = [sys.stdin.readline().strip() for _ in range(n)]
friend = [0]

def loop(price, friend):
    ret = [len(friend)]
    for f in range(1,n):
        if f not in friend and a[friend[-1]][f] >= price:
            friend.append(f)
            ret.append(loop(a[friend[-2]][f], friend))
            friend.pop()
    return max(ret)

ret = []
for i in range(1,n):
    friend.append(i)
    ret.append(loop(a[0][i], friend))
    friend.pop()
print(max(ret))