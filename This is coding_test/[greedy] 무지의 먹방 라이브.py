def solution(food_times, k):
    answer = 0
    sum_count = 0
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