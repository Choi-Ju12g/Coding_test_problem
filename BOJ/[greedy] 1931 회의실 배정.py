n = int(input())
time = []

for _ in range(n):
    start, end = map(int, input().split())
    time.append([start,end])
time.sort(key=lambda x:x[0])
time.sort(key=lambda x:x[1])
#time.sort(key=lambda x:(x[1],x[0]))

count = 0
last = 0
for cur in time:
    if cur[0] > last:
        count += 1
        last = cur[1]


print(count)