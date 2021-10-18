from collections import deque

move =[(1,0),(0,-1),(-1,0),(0,1)]

# place : 5*5 matrix, x:시작 위치 x좌표, y:시작 위치 y좌표
def bfs(place,x,y):
    visited = [[0]*5 for i in range(5)]
    que = deque()
    que.append([x,y,0])  # (x,y)에 거리 0
    visited[x][y] = 1  # 시작 위치 방문처리

    while que:
        pos = que.popleft()

        if (pos[2] == 1 or pos[2] == 2) and place[pos[0]][pos[1]] == 'P':
            return False

        for i in range(len(move)):
            #매번 다음 위치 값 저장
            dPos =[0,0,0]
            dPos[0] = pos[0] + move[i][0]
            dPos[1] = pos[1] + move[i][1]
            dPos[2] = pos[2] +1

            # 맵 범위 벗어나는 경우 제외
            if 0<= dPos[0] < 5 and 0<= dPos[1]<5:
                if place[dPos[0]][dPos[1]] != "X" and visited[dPos[0]][dPos[1]] ==0:
                    que.append(dPos)
                    visited[dPos[0]][dPos[1]] = 1
        # 거리가 3이상이면 true
        if pos[2] > 2:
            break
    return True

def solution(places):
    answer = []
    bool = True
    for place in places:
        bool = True
        for x in range(len(place)):

            for y in range(len(place[0])):
                if place[x][y] == "P":
                    if bfs(place,x,y) == False:
                        bool = False
                        break
            if bool == False:
                break
        if bool == False:
            answer.append(0)
        else:
            answer.append(1)

    return answer

places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

solution(places)