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
    #print("up down"+str(answer))
    if 0 not in charset:
        answer += len(name)-1
    else:
        next = charset.index(0) +1
        while next < len(name) and charset[next] == 0:
            next += 1
        if charset.index(0) > 1:
            answer += min(len(name)-1, (2*charset.index(0)+len(name)-next))
        else:
            answer += min(len(name)-1, len(name)-next)
    return answer

print(solution("ABAAAAAAAAABB"))

# 모범답안
def solution(name):
    answer = 0
    min_move = len(name) - 1
    next = 0

    for i, char in enumerate(name):
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)

        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1

        min_move = min(min_move, i + i + len(name) - next)
    answer += min_move
    return answer