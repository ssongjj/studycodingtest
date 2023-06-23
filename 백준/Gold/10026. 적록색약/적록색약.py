import sys

sys.setrecursionlimit(10000)

def dfs(x, y, color, is_color_weak):
    visited[x][y] = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue

        if is_color_weak and area[nx][ny] == "G":
            area[nx][ny] = "R"

        if not visited[nx][ny] and area[nx][ny] == color:
            dfs(nx, ny, area[nx][ny], is_color_weak)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


n = int(input())
area = [list(input()) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

normal_cnt = 0
color_weak_cnt = 0

#색약이 아닐 때는 r과 g를 구분해서 처리
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i, j, area[i][j], False)
            normal_cnt += 1

visited = [[0] * n for _ in range(n)]

#색약일 때는 r과 g를 동일하게 처리
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            if area[i][j] == "G":
                area[i][j] = "R"
            dfs(i, j, area[i][j], True)
            color_weak_cnt += 1

print(normal_cnt, color_weak_cnt)