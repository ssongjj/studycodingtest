from collections import deque
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, maps):
    que = deque() # x, y, cnt
    que.append((x, y, 1))
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]
    visited[x][y] = True
    
    while que:
        x, y, cnt = que.popleft()
        
        if x == len(maps) - 1 and y == len(maps[0]) - 1:
            return cnt
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]):
                if maps[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    que.append((nx, ny, cnt + 1))
    return -1
                

def solution(maps):
    return bfs(0, 0, maps)