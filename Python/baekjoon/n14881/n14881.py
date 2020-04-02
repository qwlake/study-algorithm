import sys

# act:
# a - 0,
# b - 1,
# 물을 채움 - ,0
# 물을 버림 - ,1
# 물을 옮김 - ,2
def loop(act, a, b, c):
    if act[1] == 0:
        loop((1), )

for _ in range(int(input())):
    a, b, c = map(int, sys.stdin.readline().split())
    