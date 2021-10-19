def solution(people, limit):
    answer = 0
    people.sort()
    j = 0
    while len(people) >= 2:
        if  people[0]+ people[-1] <= limit:
            people.pop()
            people.pop(0)
            answer+=1
        else:
            people.pop()
            answer+=1
    if len(people) == 1:
        answer +=1
    return answer