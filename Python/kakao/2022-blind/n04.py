def calculate(info, my):
    score = [0, 0]
    for i in range(10):
        if info[i] > 0 or my[i] > 0:
            score[int(bool(info[i] >= my[i]))] += (10 - i)
    return score[0] - score[1]


def comp(arr1, arr2):
    for i in range(len(arr1) - 1, -1, -1):
        if arr1[i] < arr2[i]:
            return arr2
        elif arr1[i] > arr2[i]:
            return arr1
    return arr1


def loop(t, n, info, my, result):
    if t == 21:
        diff = calculate(info, my)
        if diff > 0:
            if n > 0:
                my[-1] += n
            if diff > result[0]:
                result[0] = diff
                result[1] = my.copy()
            elif diff == result[0]:
                result[1] = comp(my, result[1]).copy()
            if n > 0:
                my[-1] -= n
        return

    hit = info[t - 10] + 1
    if n >= hit:
        my[t - 10] += hit
        loop(t + 1, n - hit, info, my, result)
        my[t - 10] -= hit

    loop(t + 1, n, info, my, result)


def solution(n, info):
    result = [0, []]

    my_hit = [0] * 11

    loop(10, n, info, my_hit, result)

    print(result)
    if not result[1]:
        return [-1]
    else:
        return result[1]


if __name__ == "__main__":
    # print(solution(5, [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]))  # [0,2,2,0,1,0,0,0,0,0,0]
    # print(solution(1, [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))  # [-1]
    print(solution(9, [0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1]))  # [1,1,2,0,1,2,2,0,0,0,0]
    # print(solution(10, [0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 3]))  # [1,1,1,1,1,1,1,1,0,0,2]
    # print(solution(10, [10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
    # print(solution(10, [2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0]))
