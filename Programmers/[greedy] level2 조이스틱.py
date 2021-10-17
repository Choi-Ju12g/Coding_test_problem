def solution(name):
    answer = 0
    standard = int(ord('A'))
    charset = []
    for i in range(len(name)):
        if int(ord(name[i])) - standard <= 13:
            charset.append(int(ord(name[i])) - standard)
            answer += int(ord(name[i])) - standard
        else:
            charset.append(26-int(ord(name[i])) + standard)
            answer += 26-int(ord(name[i])) + standard
    print("up down"+str(answer))
    if 0 not in charset:
        answer += len(name)-1
    else:
        next = charset.index(0) +1
        while next < len(name) and charset[next] == 0:
            next += 1
        answer += min(len(name)-1, (2*charset.index(0)+len(name)-next))
    return answer

print(solution("JAN"))