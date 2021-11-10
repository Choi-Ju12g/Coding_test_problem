def solution(record):
    answer = []
    ID = dict()  # key 값으로 value를 찾기 용이
    list = []

    for data in record:
        s = data.split()
        verb = s[0]
        id = s[1]

        if verb in ["Enter", "Change"]:
            nickname = s[2]
            ID[id] = nickname
        list.append((verb, id))

    for i in list:
        if i[0] == 'Enter':
            # answer.append(f'{ID[i[1]]}님이 들어왔습니다.')
            answer.append('%s님이 들어왔습니다.' % ID[i[1]])
        elif i[0] == 'Leave':
            answer.append('%s님이 나갔습니다.' % ID[i[1]])

    return answer

string = "adsfklj"
str = []

str.append(f'{string} is string?')
print(str)