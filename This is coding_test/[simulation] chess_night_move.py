n = input()
x = int(n[1])
y = int(ord(n[0])-96)
cnt = 0

# 움직임 정의 방법 1
dx = [-2,-2,-1,1,2,2,1,-1]
dy = [-1,1,2,2,1,-1,-2,-2]
move_types = ['A','B','C','D','E','F','G','H']

# 이동 지정
for move in range(len(move_types)):
    #이동 방향 정립
    nx = x + dx[move]
    ny = y + dy[move]

    if nx < 1 or ny <1 or nx >8 or ny > 8:
        continue
    cnt +=1

# 움직임 정의 방법 2
move_types2 = [(-2,-1),(-2,1),(-1,2),(1,2),
               (2,1),(2,-1),(1,-2),(-1,-2)]

for move in range(move_types2):
    nx = x + move[0]
    ny = y + move[1]

    if nx >= 1 and ny >= 1 and nx <= 8 and ny <= 8:
        continue
    cnt += 1

print(cnt)

# for moves in range(move_types):
#     nx = x - move[0]
#     ny = y - move[1]
#
#     if nx >= 1 and ny >= 1:
#         continue
#     cnt += 1
