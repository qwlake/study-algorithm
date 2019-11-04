import sys

def calc(hi, h):
    sum = 0
    for i in range(len(hi)-1):
        if h >= hi[i] and h >= hi[i+1]:
            if hi[i] <= hi[i+1]:
                sum += h - hi[i+1]
                sum += (hi[i+1] - hi[i]) / 2
            else:
                sum += h - hi[i]
                sum += (hi[i] - hi[i+1]) / 2
        elif h > hi[i] and h < hi[i+1]:
            sum += (h-hi[i])**2 / (2 * (hi[i+1] + hi[i]))
        elif h < hi[i] and h > hi[i + 1]:
            sum += (h - hi[i+1]) ** 2 / (2 * (hi[i + 1] + hi[i]))
    return sum


N, M = [int(i) for i in sys.stdin.readline().split(" ")]
Hi = [int(i) for i in sys.stdin.readline().split(" ")]
turn = 0
h = 0
while turn < M:
    temp_input = sys.stdin.readline()
    if temp_input[0] == 'Q':
        turn += 1
        h = int(temp_input.split(" ")[1])
        print("%.3f" % calc(Hi, h))
    elif temp_input[0] == 'U':
        Hi[int(temp_input.split(" ")[1])] = int(temp_input.split(" ")[2])