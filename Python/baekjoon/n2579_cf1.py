# -*- coding: utf-8 -*-

a = int(input())

stair = []
matrix = [[0] * 5 for i in range(0, a + 1)]


for i in range(0, a):
    stair.append(int(input()))

for i in range(1, a+1):
    matrix[i][0] = matrix[i-1][1] + stair[i-1]
    matrix[i][1] = matrix[i-1][2] + stair[i-1]
    matrix[i][2] = max(matrix[i-1][1], matrix[i-1][0])

print(max(matrix[i][1], matrix[i][0]))

print(matrix)