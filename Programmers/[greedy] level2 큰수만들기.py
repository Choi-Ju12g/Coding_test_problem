def solution(number, k):
    answer = ''
    temp = number
    sort_list = []
    while temp > 0:
        sort_list.append(temp%10)
        temp //= 10
    sort_list.sort(reverse=True)
    for i in range(k):
        sort_list.pop()

    for i in range(len(sort_list)):
        answer += str(sort_list[i])

    return answer

solution(1924,2)