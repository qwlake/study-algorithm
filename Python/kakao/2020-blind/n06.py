def merge(diff_dist, d):
    sidx = 0
    eidx = 2
    ms = 0
    me = 2
    maximum = 0
    dist_cnt = 3
    while dist_cnt <= len(diff_dist):
        s = sum(diff_dist[sidx : eidx+1 % len(diff_dist)])
        can = sum(diff_dist[sidx+1 : eidx % len(diff_dist)])
        if s > maximum:
            maximum = s
            ms = sidx
            me = eidx
        if can + diff_dist[eidx % len(diff_dist)] > d:
            if sidx+1 == len(diff_dist):
                break
            sidx += 1
            can -= diff_dist[sidx]
            dist_cnt -= 1
        dist_cnt += 1
        eidx += 1

    sidx = ms
    eidx = me

    if eidx >= len(diff_dist):
        diff_dist = diff_dist[eidx+1:sidx] + [maximum]
    else:
        front = diff_dist[:sidx] + [maximum]
        if eidx == len(diff_dist)-1:
            back = []
        else:
            back = diff_dist[eidx+1:]
        diff_dist = front+back
    
    return diff_dist

def loop(diff_dist, dist, cnt):
    if len(diff_dist) == 1:
        if len(dist) > 0:
            return cnt
        else:
            return -1
    elif len(diff_dist) == 2:
        m = min(diff_dist)
        if len(dist) > 0:
            if dist[0] >= m:
                return cnt+1
        return -1
    diff_dist = merge(diff_dist, dist.pop(0))
    return loop(diff_dist, dist, cnt+1)

def solution(n, weak, dist):
    if len(weak) == 1:
        return 1

    first = weak[0]
    for i in range(len(weak)):
        weak[i] -= first

    dist = sorted(dist, reverse=True)

    diff_dist = []
    for i in range(len(weak)-1):
        diff = weak[i+1] - weak[i]
        diff_dist.append(diff)
    diff = n-weak[-1]
    diff_dist.append(diff)

    answer = loop(diff_dist, dist, 0)

    return answer

a = solution(
    12,
    [1, 5, 6, 10],
    [1, 2, 3, 4]
) # 2
print(a)

a = solution(
    12,
    [1, 3, 4, 9, 10],
    [3, 5, 7]
) # 1
print(a)