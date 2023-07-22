import itertools 

def solution(n):
    #나선형의 배열을 생성
    snail = [[0] * i for i in range(1, n+1)]
    
    dx = [0, 1, -1]
    dy = [1, 0, -1]
    x = y = angle = 0
    cnt = 1
    size = (n+1)*n//2
    
    while cnt <= size:
        snail[y][x] = cnt
        ny = y + dy[angle]
        nx = x + dx[angle]
        cnt += 1
        
        #배열 끝에 닿으면 방향 변경
        if 0 <= nx <= ny and 0 <= ny < n and snail[ny][nx] == 0:
            y, x = ny, nx
        else:
            angle = (angle+1) % 3
            y += dy[angle]
            x += dx[angle]
    answer = list(itertools.chain(*snail))
    
    return answer