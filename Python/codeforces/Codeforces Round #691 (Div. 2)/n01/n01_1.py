from itertools import permutations
import sys

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    red = list(sys.stdin.readline().strip())
    blue = list(sys.stdin.readline().strip())
    if red == blue:
        print("EQUAL")
        continue
    combi_r = list(permutations(red, n))
    combi_b = list(permutations(blue, n))
    red_win, blue_win = 0, 0
    for r, b in zip(combi_r, combi_b):
        
        for i in range(len(r)):
            if r[i] < b[i]:
                blue_win += 1
                break
            elif r[i] > b[i]:
                red_win += 1
                break
        # r_int, b_int = int(''.join(r)), int(''.join(b))
        # if r_int < b_int:
        #     blue_win += 1
        # elif r_int > b_int:
        #     red_win += 1
    if red_win < blue_win:
        print("BLUE")
    elif red_win > blue_win:
        print("RED")
    else:
        print("EQUAL")