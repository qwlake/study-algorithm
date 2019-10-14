T = int(input())
n_list = [_ for _ in range(T)]
for i in range(T):
    n_list[i] = int(input())
n_result = [1, 2, 4]

for i in range(3, max(n_list)):
    n_result.append(n_result[i-3] + n_result[i-2] + n_result[i-1])

for i in n_list:
    print(n_result[i-1])