# -*- coding: utf-8 -*-
import array

def loop(row, col, queens):
#		for (int i = 0; i < number; i++) { for (int j = 0; j < number; j++) {
#		System.out.print(pan[i][j]); } System.out.println(); } System.out.println();
    if queens == N:
        global count
        count += 1
        return
    elif row < N:
        for i in range(N):
            if arr[row][i] >= 0:
                possible_change(row, i, -1)
                loop(row + 1, 0, queens + 1)
                possible_change(row, i, 1)

def possible_change(row, col, sub):
    for i in range(N):
        arr[row][i] += sub
    for i in range(N):
        arr[i][col] += sub
    for i in range(len(directions)):
        tempRow = row
        tempCol = col
        while (tempRow >= 0 and tempRow < N and tempCol >= 0 and tempCol < N):
            arr[tempRow][tempCol] += sub
            tempRow += directions[i][0]
            tempCol += directions[i][1]
        for j in range(0, 5):
            arr[row][col] -= sub

while True:
    directions = ((-1, 1), (1, 1), (1, -1), (-1, -1))
    count = 0
    N = int(input())    # (1 ≤ N < 15)
    arr = [array.array('i') for i in range(N)]
    for row in arr:
        for j in range(0, N):
            row.append(0)
    loop(0, 0, 0)
    print(count)