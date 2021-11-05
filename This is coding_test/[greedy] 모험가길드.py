N = int(input())
Scares = list(map(int,input().split()))
Scares.sort()

result = 0
count = 0

for i in Scares:
    count+=1
    if count >= i:
        result+=1
        count = 0

print(result)

