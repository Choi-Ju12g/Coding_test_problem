n = int(input())

target = 0
while n >= 0:
    if n % 5 == 0:
        target += n//5
        print(target)
        break
    n -= 3
    target +=1
else:
    print(-1)