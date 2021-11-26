def solution(food_times, k):
    answer = 0
    pivot = 0
    if sum(food_times) <= k:
        return -1

    for i in range(k + 1):
        if food_times[pivot] > 0:
            food_times[pivot] -= 1
            pivot = (pivot + 1) % len(food_times)
        else:
            pivot = (pivot + 1) % len(food_times)
            i -= 1
    answer = pivot + 1
    return answer

import heapq

def solution(food_times,k):
    if sum(food_times) <= k:
        return -1

    q = []
    for i in range(len(food_times)):
        heapq.heappush(q,(food_times[i], i+1))

    sum_value = 0
    previous = 0
    length = len(food_times)

    while sum_value + ((q[0][0]-previous)*length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length
        length -= 1
        previous = now

    result = sorted(q, key=lambda x:x[1])
    return result[(k-sum_value)%length][1]