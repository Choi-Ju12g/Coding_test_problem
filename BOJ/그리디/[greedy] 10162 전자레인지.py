menu = [300,60,10]


def cal():
    n = int(input())
    count = []
    if n% 10 != 0:
        print(-1)
    else:
        for i in menu:
            count.append(n//i)
            n %= i
    print(count[0], count[1], count[2])

cal()
