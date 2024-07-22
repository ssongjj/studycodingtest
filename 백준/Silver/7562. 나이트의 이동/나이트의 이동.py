from collections import deque
import sys

input = sys.stdin.readline

dx = [1, 1, 2, 2, -1, -1, -2, -2]
dy = [-2, 2, -1, 1, -2, 2, -1, 1]


def bfs(x, y):
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()

        if x == ex and y == ey:
            return chess_map[x][y]

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < l and 0 <= ny < l and chess_map[nx][ny] == 0:
                q.append((nx, ny))
                chess_map[nx][ny] = chess_map[x][y] + 1


for _ in range(int(input())): 
    l = int(input())
    chess_map = [[0] * l for _ in range(l)]
    sx, sy = map(int, input().split()) 
    ex, ey = map(int, input().split())  
    print(bfs(sx, sy))