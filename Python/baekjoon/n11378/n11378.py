# -*- coding: utf-8 -*-

first = input().split(" ")
N, M, K = int(first[0]), int(first[1]), int(first[2])
possible = []
possible_count = []
works_count = [0 for _ in range(M)]
for i in range(N):
    second = input().split(" ")
    possible_count.append(int(second[0]))
    temp = [int(second[p+1]) for p in range(possible_count[i])]
    possible.append(temp)
    for j in temp:
        works_count[j-1] += 1

while True:
    p_max = possible_count.index(max(possible_count))
    temp = possible[p_max]
    sort = sorted(range(len(temp)), key=lambda k: temp[k])
    for i in sort:
        