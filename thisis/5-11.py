from collections import deque
n, m = map(int, input().split())
array = []

for _ in range(n):
    array.append(list(map(int, input())))

visited = [[False] * m for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

queue = deque()

def bfs(x, y):
    queue.append((x, y))

    while queue:
        mx, my = queue.popleft()

        if not visited[mx][my]:
            visited[mx][my] = True
            for i in range(4):
                 nx = mx + dx[i]
                 ny = my + dy[i]

                 if 0<= nx < n and 0<= ny < m:
                     if array[nx][ny] == 1 and not visited[nx][ny]:
                         array[nx][ny] = array[mx][my] + 1
                         queue.append((nx, ny))
    return array[n-1][m-1]

print(bfs(0,0))