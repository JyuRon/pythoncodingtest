n, m = map(int, input().split())
#
array = []
for _ in range(n):
    array.append(list(input()))

# array = [['0', '0', '1', '1', '0'], ['0', '0', '0', '1', '1'], ['1', '1', '1', '1', '1'], ['0', '0', '0', '0', '0']]
visited = [[False] * m for _ in range(n)]
move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
result = 0

def dfs(x, y):
    visited[x][y] = True

    for i in move:
        dx = x + i[0]
        dy = y + i[1]
        if 0 <= dx < n and 0 <= dy < m:
            if array[dx][dy] == '0' and not visited[dx][dy]:
                dfs(dx, dy)


for i in range(n):
    for j in range(m):
        if not visited[i][j] and array[i][j] == '0':
            dfs(i, j)
            result += 1

print(result)
