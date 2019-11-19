
def ev(a,b,c):
    return eval(str(a)+b+str(c))

def loop(a, num, idx1, idx2):
    tmp = 0
    if idx2-idx1 == 4:
        tmp = ev(a[idx2-2], a[idx2-1], a[idx2])
        tmp = ev(num, a[idx2-3], tmp)
    else:
        tmp = ev(num, a[idx2-1], a[idx2])
    if idx2 == N-1:
        return tmp
    x = loop(a, tmp, idx2, idx2+2)
    y = loop(a, tmp, idx2, idx2+4) if idx2+4 < N else x
    return max(x,y)

N = int(input())
a = [int(e) if i%2==0 else e for i, e in enumerate(list(input()))]

if N == 1:
    print(a[0])
elif N == 3:
    print(ev(a[0], a[1], a[2]))
else:
    print(max(loop(a, a[0], 0, 4), loop(a, a[0], 0, 2)))
