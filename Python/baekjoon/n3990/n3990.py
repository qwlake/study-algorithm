N, M = [int(i) for i in input().split(" ")]
Hi = [int(i) for i in input().split(" ")]
turn = 0
h = 0
while turn < M:
    temp_input = input()
    if temp_input[0] == 'Q':
        turn += 1
        h = int(temp_input.split(" ")[1])
        calc(Hi, h)
    elif temp_input[0] == 'U':
        Hi[int(temp_input.split(" ")[1])] = int(temp_input.split(" ")[2])

def calc(hi, h):
    for i in range(len(hi)-1):
        if h > hi[i] and h > hi[i+1]:
            if hi[i] <= hi[i+1]:
                sqr = (h - hi[i+1]) * (h - hi[i+1])
                tri =
            else:
                sqr = (hi[i+1] - h) * (hi[i+1] - h)
