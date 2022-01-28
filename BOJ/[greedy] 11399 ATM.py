n =  int(input())
data = list(map(int, input().split()))
data.sort()

result = 0
length = len(data)
for i in range(length):
    result += data[i]*(length-i)
print(result)