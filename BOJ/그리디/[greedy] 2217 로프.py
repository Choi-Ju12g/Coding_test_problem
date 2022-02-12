n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
a.sort(reverse=True)
maximum = a[0]
for i in range(n):
    maximum = max(maximum,a[i]*(i+1))
print(maximum)

