# -*- coding: utf-8 -*-

first = input().split(" ")
N, M, K = int(first[0]), int(first[1]), int(first[2])
possible = []
possible_count = []
works_count = [0 for _ in range(M)]
check = [0 for _ in range(M)]

for i in range(N):
    second = input().split(" ")
    possible_count.append(int(second[0]))
    temp = [int(second[p+1]) for p in range(possible_count[i])]
    possible.append(temp)
    for j in temp:
        works_count[j-1] += 1
        
sort = sorted(range(len(possible_count)), key=lambda k: possible_count[k], reverse=True)

for i in sort:
    p_max = i
    sort_to_index = sorted(range(len(works_count)), key=lambda k: works_count[k])
    p_works = sort_to_index[-len(possible[p_max]):]
    for j in p_works:
        if check[j] == 0:
            check[j] = 1
            if possible_count[p_max] > 0:
                possible_count[p_max] -= 1
            elif K > 0:
                K -= 1
            else:
                check[j] = 0
                break
                
count = 0
for i in check:
    if i == 1:
        count += 1
print(count)