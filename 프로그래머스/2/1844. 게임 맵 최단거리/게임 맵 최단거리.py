from collections import deque
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, maps):
    que = deque() # x, y
    que.append((x, y))
    
    while que:
        x, y = que.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= len(maps) or ny < 0 or ny >= len(maps[0]): 
                continue
                
            if maps[nx][ny] == 0:
                continue
            
            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                que.append((nx, ny))

    return maps[len(maps) - 1][len(maps[0]) - 1]
                

def solution(maps):
    answer = bfs(0, 0, maps)
    if answer == 1:
        return -1

    return answer