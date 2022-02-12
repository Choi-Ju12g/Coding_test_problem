n , k = map(int,input().split())
data = [int(input()) for _ in range(n)]
count = 0

while k > 0:
    if data[-1] > k:
        data.pop(-1)
    else:
        count += k//data[-1]
        k %= data[-1]
print(count)