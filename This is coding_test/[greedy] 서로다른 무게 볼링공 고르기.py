N, M = list(input().split())
data = list(map(int,input().split()))
data.sort()

result = 0
pivot = 0
for i in range(len(data)-1):
    for j in range(i+1,len(data)):
        if data[i] != data[j]:
            result += 1

print(result)