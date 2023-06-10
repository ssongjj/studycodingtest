from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, maps):
    que = deque()
    que.append((x, y))
    
    while que:
        x, y = que.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            #맵을 벗어나면 무시
            if nx < 0 or nx >= len(maps) or ny < 0 or ny >= len(maps[0]): 
                continue
            
            #벽이면 무시
            if maps[nx][ny] == 0:
                continue
                
            #처음 지나가는 길이면 거리 계산 후 상하좌우 확인
            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                que.append((nx, ny))
    return maps[len(maps)-1][len(maps[0])-1]

def solution(maps):
    answer = 0 
    #상대팀의 진영에 도착할 수 없을 때는 -1
    #상대팀의 진영으로 가기 위해 이동해야 하는 칸의 최솟값
    answer = bfs(0, 0, maps)
    
    if answer == 1:
        return -1
    
    return answer