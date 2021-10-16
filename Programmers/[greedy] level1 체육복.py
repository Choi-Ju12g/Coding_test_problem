def solution(n, lost, reserve):
    answer = 0
    count = 0
    for i in range(len(lost)):
        a, b = lost[i] - 1, lost[i] + 1
        for j in range(len(reserve)):
            if reserve[j] == a:
                count += 1
                del reserve[j]
                break
            elif reserve[j] == b:
                count += 1
                del reserve[j]
                break

    answer = n - len(lost) + count
    return answer
