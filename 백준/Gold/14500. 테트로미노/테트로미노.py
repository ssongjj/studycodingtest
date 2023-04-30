import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, step, total):
    global n, m, answer, max_value

    if total + max_value * (4 - step) <= answer:
        return

    if step == 4:
        answer = max(answer, total)
        return

    for i in range(4):
        nx, ny = x+ dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            if step == 2: #ㅗ 이 모양 때문에 따로 처리해 줌
                visited[nx][ny] = True
                dfs(x, y, step+1, total+a[nx][ny]) #nx, ny가 아닌 다시 제자리에서 재귀할 수 있도록
                visited[nx][ny] = False
            visited[nx][ny] = True
            dfs(nx, ny, step+1, total+a[nx][ny])
            visited[nx][ny]= False

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

visited = [[False] * m for _ in range(n)]
answer =0
max_value = max(map(max, a))

for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i, j, 1, a[i][j])
        visited[i][j] = False

print(answer)