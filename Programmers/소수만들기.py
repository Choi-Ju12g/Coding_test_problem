from itertools import combinations

def is_prime_num(num):
    if num == 0 or num == 1:
        return False
    else:
        for i in range(2, (num//2)+1):
            if num% i == 0:
                return False
        return True

def solution(nums):
    answer = 0
    num_set = list(combinations(nums,3))
    for i in num_set:
        if is_prime_num(sum(i)):
            answer+=1

    return answer
#print(is_prime_num(29))
#solution([1,2,3,4,5])

def sieve(n):
    """
    에라토스테네스의 체
    소수를 적고 해당 수의 배수를 싹 지우는 방식
    """
    if n < 2:
        return []

    #[0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1] ->순서대로 0 1 2 3 4 5 6 인데 0이면 소수가 아님 1이면 소수임 으로 시작
    s = [0, 0] + [1] * (n - 1)

    for i in range(2, int(n**.5)+1):
        if s[i]:
            s[i*2::i] = [0] * ((n - i)//i)
    return [i for i, v in enumerate(s) if v]

def solution(nums):
    primes = sieve(3000)

    count = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                if (nums[i] + nums[j] + nums[k]) in primes:
                    count += 1

    return count
