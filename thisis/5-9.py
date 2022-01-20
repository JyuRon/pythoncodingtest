from collections import deque
graph = [[],[2,3,8],[1,7],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]]
visited = [False] * 9
needVisited = deque()
def bfs(graph, node, visited):
    needVisited.append(node)

    while needVisited:
        v = needVisited.popleft()

        if not visited[v]:
            print(v, end=' ')
            visited[v] = True
            needVisited.extend(graph[v])


bfs(graph,1,visited)