GET_NUM = 4
ret_list = []
def loop(arr, x, ret):
    arr.remove(x)
    ret.append(x)
    if len(ret) == GET_NUM:
        return ret
    for i in arr:
        temp = loop(arr.copy(), i, ret.copy())
        if temp is not None:
            ret_list.append(temp)

n = int(input())
arr = [i for i in range(n)]
for i in range(n):
    loop(arr.copy(), i, [])

print(ret_list)