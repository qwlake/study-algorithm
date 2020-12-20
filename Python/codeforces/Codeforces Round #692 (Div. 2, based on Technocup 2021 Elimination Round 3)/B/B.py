import sys

for _ in range(int(sys.stdin.readline())):
    n = sys.stdin.readline().strip()
    tmp = int(n)
    n = set(list(map(int, n)))
    while True:
        is_success = True
        for i in n:
            if i != 0 and tmp % i != 0:
                is_success = False
        if is_success:
            print(tmp)
            break
        else:
            tmp += 1
            n = set(list(map(int, str(tmp))))
