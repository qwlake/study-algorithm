def solution(k, room_number):
    answer = []
    room_dic = dict()
    for rm in room_number:
        if rm not in room_dic.keys():
            room_dic[rm] = rm+1
            answer.append(rm)
        else:
            i = rm
            key_list = []
            while i in room_dic.keys():
                key_list.append(i)
                i = room_dic[i]
            room_dic[i] = i+1
            for key in key_list:
                room_dic[key] = i+1
            answer.append(i)
        print(room_dic)
    return answer

if __name__ == "__main__":
    ans = solution(10, [1,3,4,1,3,1])
    # ans = solution(100, (1,1,1,1,5,5,5,5,3))
    print(ans)