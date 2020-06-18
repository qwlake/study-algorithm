def is_valid(p:str) -> bool:
    stack = 0
    for i in range(len(p)):
        if p[i] == '(':
            stack += 1
        else:
            stack -= 1
        if stack < 0:
            return False
    return True

def split_uv(w:str) -> (str, str):
    s_cnt, e_cnt = 0, 0
    for i in range(len(w)):
        if w[i] == '(':
            s_cnt += 1
        else:
            e_cnt += 1
        if s_cnt == e_cnt:
            return w[:i+1], w[i+1:]

def modify(u:str, v:str) -> str:
    ret = '(' + v + ')'
    for s in u[1:len(u)-1]:
        if s == '(':
            ret += ')'
        else:
            ret += '('
    return ret

def loop(w:str) -> str:
    if w == '':
        return ''
    u, v = split_uv(w)
    if is_valid(u):
        ret = loop(v)
        ret = '' if ret == None else ret
        return u + ret
    else:
        ret = modify(u, loop(v))
        return ret

def solution(p):
    answer = loop(p)
    return answer

a = solution("()))((()") # "()(())()"
print(a)
