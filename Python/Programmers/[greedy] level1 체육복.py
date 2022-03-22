def solution(n, lost, reserve):
    answer = 0
    r_lost = list(set(lost)-set(reserve))
    r_reserve = list(set(reserve)-set(lost))
    for i in r_reserve:
        if i-1 in r_lost:
            r_lost.remove(i-1)
        elif i+1 in r_lost:
            r_lost.remove(i+1)
    answer = n -len(r_lost)
    # count = 0
    #
    # # lost와 reserve 동일한 값 제거
    # lost = list(set(lost) - set(reserve))
    # reserve = list(set(reserve) - set(lost))
    #
    # # 빌려줄 수 있는 수 계산
    # answer = n - len(lost)
    # for i in range(len(lost)):
    #     a = lost.pop()
    #
    #     check = False
    #     for j in range(len(reserve)):
    #         if reserve[j] == a - 1:
    #             del reserve[j]
    #             check = True
    #             count += 1
    #             break
    #     if not check:
    #         for j in range(len(reserve)):
    #             if reserve[j] == a + 1:
    #                 del reserve[j]
    #                 count += 1
    #                 break
    # answer += count

    return answer