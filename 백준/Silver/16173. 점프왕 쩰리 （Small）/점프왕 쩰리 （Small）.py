def jelly_game(N, game_map):
    visited = [[False] * N for _ in range(N)]

    def dfs(x, y):
        # 게임판의 범위를 벗어나거나 이미 방문한 경우
        if x < 0 or x >= N or y < 0 or y >= N or visited[x][y]:
            return False

        # 끝 점에 도달한 경우
        if game_map[x][y] == -1:
            return True

        # 현재 칸에 적힌 수
        num = game_map[x][y]
        visited[x][y] = True

        # 오른쪽으로 이동
        if dfs(x, y + num):
            return True

        # 아래로 이동
        if dfs(x + num, y):
            return True

        return False

    return "HaruHaru" if dfs(0, 0) else "Hing"

N = int(input())
game_map = []
for _ in range(N):
    row = list(map(int, input().split()))
    game_map.append(row)

print(jelly_game(N, game_map))