import re

def loop(bans_list, id_list, res):
    ret = list()
    for i, bans in enumerate(bans_list):
        for ban in bans:
            if id_list[int(ban)] == 0:
                if len(bans_list) == 1:
                    tmp = sorted(res+[ban])
                    ret.append("".join(tmp))
                else:
                    id_list[int(ban)] = 1
                    r = loop(bans_list[:i]+bans_list[i+1:], id_list, res+[ban])
                    ret += r
                    id_list[int(ban)] = 0
    return list(set(ret))

def solution(user_id, banned_id):
    if len(user_id) == len(banned_id):
        return 1
    for i in range(len(banned_id)):
        banned_id[i] = banned_id[i].replace("*", ".")
    id_list = [0]*len(user_id)
    bans_list = list()
    for ban in banned_id:
        regex = re.compile(f'^{ban}$')
        tmp_list = []
        for i, user in enumerate(user_id):
            if regex.match(user):
                tmp_list.append(str(i))
        bans_list.append(tmp_list)
    ret = loop(bans_list, id_list, list())
    return len(ret)

if __name__ == "__main__":
    # ans = solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],
    #                 ["fr*d*", "*rodo", "******", "******"])
    # print(ans)
    ans = solution(["frodo11", "fradi1", "crodo1", "abc12", "frod1", "frod2", "frod3", "frod4"],
                    ["*******", "******", "******", "*****", "*****", "*****", "*****", "*****"])
    print(ans)