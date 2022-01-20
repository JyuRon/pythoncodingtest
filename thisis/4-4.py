n, m = map(int, input().split())
x, y, show = map(int, input().split())

world = []
for _ in range(n):
    world.append(list(map(int, input().split())))

visited = [[0]*m for _ in range(n)]
direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]


visited[x][y] = 1
result = 1
turnCount = 0
while True:
    show -= 1
    if show == -1:
        show = 3

    dx = x + direction[show][0]
    dy = y + direction[show][1]

    if visited[dx][dy] == 0 and world[dx][dy] == 0:
        x = dx
        y = dy
        visited[x][y] = 1
        result += 1
        turnCount = 0
    else:
        turnCount += 1

    if turnCount == 4:
        dx = x - direction[show][0]
        dy = x - direction[show][1]

        if world[dx][dy] == 0:
            x, y = dx, dy
        else:
            break
        turnCount = 0

print(result)






