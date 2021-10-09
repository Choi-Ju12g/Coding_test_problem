#N*M의 행렬에서 먼저 1개의 행을 고른뒤 해당 행 중 가장 작은 카드를 고르는 방식일때 가장 큰 카드 고르는 방법

N, M = 3, 3
data = [[3,1,2],[4,1,4],[2,2,2]]

result = 0
for i in range(N):
    print(data[i])
    min_value = min(data[i])
    result = max(min_value,result)

print(result)

'''
#n,m 을 공백으로 구분하여 입력받기
n,m = map(int,input.split())

result = 0
#한줄 씩 입력받아 확인

for i in range(n):
    data = list(map(int, input.split())
    # 현재 행에서 가장 작은값
    min_value = min(data)
    
    # 각 행의 최소값중 최대값
    result = max(result, min_value)
    
'''
