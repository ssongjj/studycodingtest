#cur 지점을 찾고 그 지점을 기준으로 주변 국가들이 l명 이상 r명 이하인지를 확인해야 함
import sys
sys.setrecursionlimit(10000)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
            diff = abs(population_area[x][y] - population_area[nx][ny])
            if l <= diff <= r:
                visited[nx][ny] = 1
                union.append((nx, ny))
                dfs(nx, ny)

n, l, r = map(int, input().split())
population_area = [list(map(int, input().split())) for _ in range(n)]

days = 0

while True:
    visited = [[0] * n for _ in range(n)]
    is_moved = False

    for i in range(n):
        for j in range(n):
            union = []

            if not visited[i][j]:
                union.append((i, j))
                visited[i][j] = 1
                dfs(i, j)

                if len(union) > 1:
                    is_moved = True
                    avg = sum([population_area[x][y] for x, y in union]) // len(union)
                    for x, y in union:
                        population_area[x][y] = avg

    if not is_moved:
        break

    days += 1

print(days)