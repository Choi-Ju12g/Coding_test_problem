
# 입력 받기
n = int(input())
dir = input().split()
print(dir)
x, y =1,1

# map list 구현
l = [[0]*7 for i in range(7)]

#  L, R, U, D
dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = ['L','R','U','D']

# 이동 계획 하나씩 진행
for move in dir:
    # 이동 후 좌표
    for i in range(4):
        if move == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    # 공간 벗어나는 경우
    if nx < 1 or ny <1 or nx > n or ny > n:
        continue

    x = nx
    y = ny
    l[x][y] = 9

print(x,y)
# 경계선 구현
for i in range(7):
    l[i][0] = 1
    l[i][6] = 1
    l[0][i] = 1
    l[6][i] = 1


# 확인용 프린트
for i in range(7):
    for j in range(7):
        print(l[i][j], end=" ")
    print()