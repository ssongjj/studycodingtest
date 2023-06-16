
# 직사각형 보드
# 빨간 구슬, 파란 구슬을 하나씩 넣는데 빨간 구슬을 꺼내는 것

# 가장 바깥 행과 열은 막혀 있고 보드에 구멍은 하나
# 빨간 구슬은 구멍에 들어가는데 파란 구슬은 들어가면 안 됨
# 좌우위아래 기울이기 dx,dy 사용 (이동 거리)
# . 빈칸 # 벽 이동 불가 O 구멍 R 빨강 B 파랑
#  NM은 3 - 10 (범위가 크지 않음)

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]



def find_init_point(board):
    rx = ry = bx = by = 0

    for i in range(n):
        for j in range(m):
            if board[i][j] == "R":
                rx, ry = i, j
            elif board[i][j] == "B":
                bx, by = i, j

    return rx, ry, bx, by

def move(board, x, y, dx, dy):
    #움직인 거리를 반환
    cnt = 0

    #움직인 곳이 벽이 아니고, 움직이기 전에 있던 곳이 구멍이 아니면
    while board[x+dx][y+dy] != "#" and board[x][y] != "O":
        x += dx
        y += dy
        cnt += 1

    return x, y, cnt

def bfs(board, rx, ry, bx, by):
    visited = set() #중복 방문은 불가하기 때문에 중복 방문을 제거를 위한 set 처리
    visited.add((rx, ry, bx, by))

    queue = deque()
    queue.append((rx, ry, bx, by, 0))

    while queue:
        rx, ry, bx, by, cnt = queue.popleft()

        if cnt >= 10:
            break

        for i in range(4):
            nrx, nry, r_cnt = move(board, rx, ry, dx[i], dy[i])
            nbx, nby, b_cnt = move(board, bx, by, dx[i], dy[i])

            #파란 구슬이 구멍에 빠지지 않은 경우를 먼저 따져 보고
            if board[nbx][nby] != "O":
                if board[nrx][nry] == "O":
                    return cnt + 1

                if (nrx, nry) == (nbx, nby): #빨강과 파랑의 위치가 같을 때 둘은 겹칠 수 없음
                    if r_cnt > b_cnt:
                        nrx -= dx[i]
                        nry -= dy[i]
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]

                if (nrx, nry, nbx, nby) not in visited: #방문한 적 없으면 방문 처리
                    visited.add((nrx, nry, nbx, nby))
                    queue.append((nrx, nry, nbx, nby, cnt+1))

    return -1 # 10 번 초과



n, m = map(int, input().split())
board = []

for _ in range(n):
    line = list(input())
    board.append(line)

#빨간 구슬과 파란 구슬 위치 탐색
rx, ry, bx, by = find_init_point(board)

print(bfs(board, rx, ry, bx, by))