from collections import deque
'''
  1
| \ \
2  8  3
| /   |\
7     4-5
|
6
'''

# 위와 같은 그래프가 있다고 할때, 인접한 노드가 여러개일 경우 낮은 수부터 방문
def dfs(graph,start_vertex,visited):
    visited[start_vertex] = True
    print(start_vertex,end=" ")

    for i in graph[start_vertex]:
        if not visited[i]:
            dfs(graph,i,visited)

def bfs(graph, start_vertex,visited):
    queue = deque()
    queue.append(start_vertex)
    visited[start_vertex] = True

    while queue:
        v = queue.popleft()
        print(v,end=" ")
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True



# 이 그래프는 인접 리스트 방식
graph = [[],[2,3,8],[1,7],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]]
visited = [False]*9
dfs(graph,1,visited)
print()
visited2 = [False]*9
bfs(graph,1,visited2)
