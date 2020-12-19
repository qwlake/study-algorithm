from itertools import permutations
import sys

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    red = list(map(int, list(sys.stdin.readline().strip())))
    blue = list(map(int, list(sys.stdin.readline().strip())))
    win_r, win_b = 0, 0
    for i in range(n):
        if red[i] < blue[i]:
            win_b += 1
        elif red[i] > blue[i]:
            win_r += 1
    if win_r == win_b:
        print("EQUAL")
    elif win_r < win_b:
        print("BLUE")
    else:
        print("RED")