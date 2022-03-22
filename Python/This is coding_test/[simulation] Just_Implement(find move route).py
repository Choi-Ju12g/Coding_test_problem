# # nXm 크기의 맵
# n, m = map(int, input().split())
#
# # 캐릭터의 x, y좌표 ,바라보는 방향 d
# x, y , d = map(int, input().split())
#
# # 서, 북, 동, 남 으로 이동
# dir = [(0,-1),(-1,0),(0,1),(1,0)]
#
# # map 정보 생성 0 : 육지, 1 : 바다, 2: 가본곳
# l = [[0]*m for _ in range(n)]
# for i in range(n):
#     x = list(map(int,input().split()))
#     for j in range(m):
#         l[i][j] = x[j]
#
# l[x][y] = 2
# cnt = 1
# turn_cnt =0
#
# while True:
#     # step 1,2
#     # 이동 할 수 있으면 이동
#     if l[x+dir[d][0]][y+dir[d][1]] == 0:
#         d += 1
#         d %=4
#         cnt += 1
#         x += dir[d][0]
#         y += dir[d][1]
#         l[x][y] = 2
#         continue
#     # 이동할 칸이 없을 경우
#     else:
#         turn_cnt +=1
#         d += 1
#         d %= 4
#         if turn_cnt == 4:
#             # 뒤로 갈 수 있는 경우
#             if l[x-dir[d][0][y-dir[d][1]]] != 1:
#                 x -= dir[d][0]
#                 y -= dir[d][1]
#             # 뒤가 바다인경우
#             else:
#                 break
#             turn_cnt =0
# print(cnt)
# 4 4
# 1 1 0
# 1 1 1 1
# 1 0 0 1
# 1 1 0 1
# 1 1 1 1


n , m = map(int, input().split())
# 방문 위치 기록용 맵
d = [[0]*m for i in range(n)]
x, y, dir = map(int, input().split())
d[x][y] = 1

# 전체 맵 정보 받기
arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))

dir_list = [(0,-1),(-1,0),(0,1),(1,0)]

# 시뮬 시작
cnt =1
turn_cnt = 0
while True:
    nx = x + dir_list[dir][0]
    ny = y + dir_list[dir][1]
    if arr[nx][ny] ==0 and d[nx][ny] ==0:
        x = nx
        y = nx
        cnt +=1
        turn_cnt = 0
        dir += 1
        dir %= 4
        d[x][y] = 1
        continue
    else :
        turn_cnt +=1
    if turn_cnt == 4:
        nx = x - dir_list[dir][0]
        ny = y - dir_list[dir][1]
        if arr[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_cnt = 0

print(cnt)