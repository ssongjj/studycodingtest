import sys

input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input())
    garden = [list(map(int, input().split())) for _ in range(n)]
    flower = [[0] * n for _ in range(n)]

    result = float('inf')
    total = 0

    # 방향 설정 (현위치, 상, 하, 좌, 우)
    dx = [0, -1, 1, 0, 0]
    dy = [0, 0, 0, -1, 1]

    #꽃이 있는지 없는지 확인
    def check_flower(x, y):
        for i in range(5):
            nx = x + dx[i]
            ny = y + dy[i]
            if flower[nx][ny] == 1:
                return False
        return True

    def cost_flower(cnt):
        global result, total

        if cnt == 3:
            result = min(result, total)
            return

        for i in range(1, n-1):
            for j in range(1, n-1):
                if check_flower(i, j):
                    #현재 위치에 꽃을 심을 수 있는 경우
                    for k in range(5):
                        x = i + dx[k]
                        y = j + dy[k]
                        flower[x][y]= 1
                        total += garden[x][y]

                    cost_flower(cnt + 1)

                    for k in range(5):
                        x = i + dx[k]
                        y = j + dy[k]
                        flower[x][y]= 0
                        total -= garden[x][y]

    cost_flower(0)
    print(result)