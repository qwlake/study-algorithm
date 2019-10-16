import sys
In = sys.stdin.readline

cnt = 0
n = In()
sum_each_num = sum(tuple(map(int, tuple(n)[:-1])))
N = int(n)
while N > 1:
    if sum_each_num % 2:
        N /= 2
        cnt += 1
    elif sum_each_num % 1:
        N -= 1
        cnt += 1
    else:
        a = N ** (1.0/2.0)
        print(N)
        print(a)
        cnt += a
        break
    sum_each_num = sum(tuple(map(int, tuple(str(N)))))
print(cnt)
