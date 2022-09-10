import math


def is_prime_number(x):
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def solution(n, k):
    answer = 0

    x = convert(n, k)
    t = x[0]
    for i in range(1, len(x)):
        if x[i] == '0':
            if t and is_prime_number(int(t)):
                answer += 1
            t = ''
        else:
            t += x[i]

    if t:
        if is_prime_number(int(t)):
            answer += 1

    return answer


def convert(n, q):
    rev_base = ''
    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)
    return rev_base[::-1]


if __name__ == '__main__':
    print(solution(
        437674,
        3)
    )

    print(solution(
        110011,
        10)
    )

