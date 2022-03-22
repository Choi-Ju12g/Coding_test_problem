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

#################################################
graph_list = {1: set([3, 4]),
              2: set([3, 4, 5]),
              3: set([1, 5]),
              4: set([1]),
              5: set([2, 6]),
              6: set([3, 5])}
root_node = 1


from collections import deque


def BFS_with_adj_list(graph, root):
    visited = []
    queue = deque([root])

    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            queue += graph[n] - set(visited)
    return visited


print(BFS_with_adj_list(graph_list, root_node))

##########################################################
def DFS_with_adj_list(graph, root):
    visited = []
    stack = [root]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            stack += graph[n] - set(visited)
    return visited

print(BFS_with_adj_list(graph_list, root_node))
##################################################