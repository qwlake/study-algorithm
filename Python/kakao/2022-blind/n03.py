import math


def convert2timestamp(t):
    h, m = map(int, t.split(':'))
    return h * 60 + m


def calculate_result(fees, duration):
    result = 0
    default, default_fee, plus, plus_fee = fees
    duration -= default
    result += default_fee
    if duration > 0:
        result += math.ceil(duration / plus) * plus_fee
    return result


def solution(fees, records):
    inout_history = dict()
    t_history = dict()
    for record in records:
        t, car_num, inout = record.split()
        if car_num not in inout_history:
            inout_history[car_num] = t
        else:
            set_duration(car_num, t_history, inout_history, t)
            del inout_history[car_num]

    for car_num in inout_history.keys():
        set_duration(car_num, t_history, inout_history, '23:59')

    result = []
    for car_num, duration in t_history.items():
        fee = calculate_result(fees, duration)
        result.append((car_num, fee))
    result.sort(key=lambda _x: _x[0])
    return list(map(lambda _x: _x[1], result))


def set_duration(car_num, t_history, inout_history, t):
    duration = convert2timestamp(t) - convert2timestamp(inout_history[car_num])
    if car_num not in t_history:
        t_history[car_num] = 0
    t_history[car_num] += duration


if __name__ == "__main__":
    print(solution([180, 5000, 10, 600],
             ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN",
              "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))  # [14600, 34400, 5000]
