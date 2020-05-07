# def solution(stones, k):
#     def find_max(arr):
#         second = largest = third = 0
#         for n in arr:
#             if n > largest:
#                 third = second
#                 second = largest
#                 largest = n
#             elif second < n < largest:
#                 third = second
#                 second = n
#             elif third < n < second:
#                 third = n
#         return largest, second, third

#     if k == 1:
#         return min(stones)
#     elif k == 2:
#         k -= 1
#         m = max(stones[0:k+1])
#         for i in range(1,len(stones)-k):
#             m = min(max(stones[i:i+k+1]), m)
#         return m
#     k -= 1
#     m1, m2, m3 = find_max(stones[0:k+1])
#     m = m1
#     for i in range(1,len(stones)-k):
#         s = set(stones[i:i+k+1])
#         if m1 not in s:
#             m1 = m2
#             m2 = m3
#         if m2 not in s:
#             m2 = m3
#         m1, m2, m3 = find_max([m1,m2,stones[i+k]])
#         m = min(m1, m)
#     return m

def solution(stones, k):
    k -= 1
    m = max(stones[0:k+1])
    for i in range(1,len(stones)-k):
        m = min(max(stones[i:i+k+1]), m)
    return m

if __name__ == "__main__":
    print(solution([2,4,5,3,2,1,4,2,5,1], 3))
    print(solution([4,4,4,10,0,0,10,4,4,4], 3))