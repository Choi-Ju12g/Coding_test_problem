# 1) n에서 1을 뺀다. 2) n을 K로 나눈다.(나누어 떨어질때만 가능) 으로 N을 1로 만드는 최소횟수

# n,k 값을 공백으로 구분하여 입력받기
#N, K = map(int, input().split)
N, K =28,5

result = N
count = 0
while  result !=1 :
    if result%K == 0 :
        result = result//K
        count +=1
    else :
        result -=1
        count += 1
print(count)