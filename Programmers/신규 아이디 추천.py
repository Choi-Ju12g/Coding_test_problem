def solution(new_id):
    answer = ''
    # step 1
    new_id = new_id.lower()

    # step 2
    origin_data = new_id
    for i in origin_data:
        if i.isalpha() or i.isdigit() or i in ['-','.','_']:
            answer += i

    # step 3
    while ".." in answer:
        answer=answer.replace('..','.')

    # step 4
    if answer[0] == '.':
        answer = answer[1:]
    if answer[-1] == '.':
        answer = answer[0:-1]

    # step 5
    if len(answer) == 0:
        answer = 'a'

    # step 6
    if len(answer) >= 16:
        answer = answer[0:15]
        if answer[-1] == '.':
            answer = answer[0:len(answer)-2]

    # step 7
    while len(answer) <= 2:
        answer += answer[-1]

    return answer