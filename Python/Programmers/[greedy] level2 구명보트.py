from collections import deque

# deque's pop(), popleft() is better than list's pop function in perspective of running time
def solution(people, limit):
    answer = 0
    people.sort()
    q = deque(people)
    while len(q) >= 2:
        if  q[0]+ q[-1] <= limit:
            q.pop()
            q.popleft()
            answer+=1
        else:
            q.pop()
            answer+=1
    if len(q) == 1:
        answer +=1
    return answer