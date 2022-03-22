def solution(numbers):
    answer = 0
    numbers.sort

    for i in numbers:
        answer += i

    answer = 45 - answer
    return answer