n = input().split(" ")

def find(num):
    a = [num]
    for i in range(1,4):
        num = num[1:]+num[0:1]
        a.append(num)
    return min(a)

n = find(n)
a = []
for i in range(int(n[0]), 0, -1):
    for j in range(int(n[1]), 0, -1):
        for k in range(int(n[2]), 0, -1):
            for l in range(int(n[3]), 0, -1):
                t = str(i)+str(j)+str(k)+str(l)
                if t == find(t):
                    a.append(t)
            n[3] = "9"
        n[2] = "9"
    n[1] = "9"
print(len(a))