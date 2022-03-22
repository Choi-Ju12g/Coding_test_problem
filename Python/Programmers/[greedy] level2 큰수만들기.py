from itertools import combinations

def solution(number,k):
    answer = []
    list = ''
    answer_len = len(str(number))-k
    for i in str(number):
        # 조건
        while answer and answer[-1] < i and k >0:
            answer.pop()
            k -= 1

        answer.append(i)
    for i in range(answer_len):
         list += answer[i]
    print(list)
    return list

solution(99994,3)


def solution_comb(number, k):
    answer = ''
    list_comb = list(combinations(list(str(number)),len(str(number))-k))
    #print(list_comb)
    list_comb.sort(reverse=True)
    answer = ''.join(list_comb[0])
    return answer



def solution_def(number,k):
    answer = ''
    temp = int(number)
    sort_list = []
    while temp > 0:
        sort_list.append(temp % 10)
        temp //= 10

    sort_list.sort(reverse=True)
    for i in range(k):
        sort_list.pop()

    for i in range(len(sort_list)):
        answer += str(sort_list[i])

    return answer

