def solution(s):
    answer = len(s)

    for w in range(1, len(s)+1):
        i = w
        cache = s[0:w]
        cnt = 1
        zipped = ''
        while i < len(s):
            if cache == s[i:i+w]:
                cnt += 1
            else:
                if cnt != 1:
                    zipped += str(cnt)
                zipped += cache
                cache = s[i:i+w]
                cnt = 1
            i += w
        if cnt != 1:
            zipped += str(cnt)
        zipped += cache
        if answer > len(zipped):
            answer = len(zipped)
    return answer

a = solution("abcabcdede") # 8
print(a)

a = solution("abcabcabcabcdededededede") # 14
print(a)