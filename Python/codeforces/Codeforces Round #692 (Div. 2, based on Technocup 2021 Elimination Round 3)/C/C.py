import sys

def move_to_center(rows, cols, row, col):
    global around_num, count
    around_num -= 1
    count += 1

    # del
    cols[rows[row]] = 0

    # move
    rows[row] = col
    cols[col] = col

    for i in range(row-1, 0, -1):
        if rows[i] != i and rows[i] != 0:
            target_pos_c = can_move_to_center(rows, cols, i)
            if target_pos_c != -1:
                move_to_center(rows, cols, i, target_pos_c)
                break


def move_to_around(rows, cols, row):
    global count
    count += 1

    col = find_pos_c(rows, cols, row)

    # del
    cols[rows[row]] = 0

    # move
    rows[row] = col
    cols[col] = row

def find_pos_c(rows, cols, row):
    for i in range(len(cols)-1, 0, -1):
        if cols[i] == 0:
            return i

def can_move_to_center(rows, cols, row):
    target_pos_c = cols[rows[row]]
    if cols[target_pos_c] == 0:
        return target_pos_c
    else:
        return -1

for _ in range(int(sys.stdin.readline())):
    n, m = map(int, sys.stdin.readline().strip().split())
    rows, cols = [0]*(n+1), [0]*(n+1)
    for _ in range(m):
        r, c = map(int, sys.stdin.readline().strip().split())
        rows[r], cols[c] = c, r
    around_num, count = 0, 0
    for i in range(1, n+1):
        if rows[i] != 0 and cols[rows[i]] != rows[i]:
            target_pos_c = can_move_to_center(rows, cols, i)
            if target_pos_c != -1:
                move_to_center(rows, cols, i, target_pos_c)
            else:
                around_num += 1
                move_to_around(rows, cols, i)
    print(count)
