import sys
input = sys.stdin.readline

# 사다리가 놓여져 있을 때 i 번째에 도착할 수 있는지 확인
# 왼쪽에 사다리가 놓였다면 -1, 오른쪽에 사다리가 놓였다면 +1
def check():
    for i in range(n):
        cur = i
        for j in range(h):
            if visited[j][cur]:
                cur += 1
            elif cur > 0 and visited[j][cur-1]:
                cur -= 1
        if cur != i: #시작 위치로 돌아오지 않았다면
            return False
    return True

#dfs를 이용
#모든 열의 사다리를 타고 이동했을 때 확인
#사다리를 놓을 수 있는 후보 위치에 다시 사다리를 놓을 수 있는지 확인
#사다리를 놓을 수 있다면 재귀
def dfs(cnt, x, y): #cnt와 x행, y행
    global answer
    if check():
        answer = min(answer, cnt)
        return #최솟값 설정 후 리턴
    elif cnt == 3 or answer <= cnt:
        return

    for i in range(x, h):
        if i == x:
            s = y  #행이 변경되지 않았다면 지금 탐색 중인 열부터
        else:
            s = 0  #행이 변경됐다면 가로선 처음부터
        for j in range(s, n-1):
            if not visited[i][j] and not visited[i][j+1]: #오른쪽 사다리가 존재하지 않는 경우
                if j > 0 and visited[i][j-1]:
                    continue
                visited[i][j] = True
                dfs(cnt+1, i, j+2)
                visited[i][j] = False

n, m, h = map(int, input().split())
visited = [[False] * (n) for _ in range(h)]  #방문 처리를 해 주기 위헤 존재


#양옆에 사다리가 있으면 사다리를 놓을 수 없다.
for _ in range(m):
    a, b = map(int, input().split())
    visited[a-1][b-1] = True #사다리 이미 있기 때문에 방문 처리

answer = 4 #최대 정답값
dfs(0, 0, 0)
print(answer if answer < 4 else -1)