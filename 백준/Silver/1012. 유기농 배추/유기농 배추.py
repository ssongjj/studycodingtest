def dfs(x, y):
    stack = [(x, y)]  # 스택을 사용하여 DFS 탐색을 구현
    field[x][y] = 0  # 방문한 배추는 0으로 표시

    while stack:
        x, y = stack.pop()

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx = x + dx
            ny = y + dy

            # 범위를 벗어나거나 배추가 없는 경우는 건너뛰기
            if nx < 0 or nx >= m or ny < 0 or ny >= n or field[nx][ny] != 1:
                continue

            stack.append((nx, ny))
            field[nx][ny] = 0  # 방문한 배추는 0으로 표시


t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split())
    field = [[0] * n for _ in range(m)]  # 배추밭 생성

    for _ in range(k):
        x, y = map(int, input().split())
        field[x][y] = 1

    worm_cnt = 0

    for i in range(m):
        for j in range(n):
            if field[i][j] == 1:
                dfs(i, j)
                worm_cnt += 1

    print(worm_cnt)