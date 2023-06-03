from collections import deque

def bfs(start, end):
    queue = deque()
    visited = [False] * 100001
    queue.append((start, 0))

    #방문 시작
    visited[start] = True

    while queue:
        cur, time = queue.popleft()

        if cur == end: #수빈이가 동생을 찾았다
            return time

        next = [cur - 1, cur + 1, cur * 2]

        for pos in next:
            if 0 <= pos <= 100000 and not visited[pos]:
                queue.append((pos, time+1))
                visited[pos] = True


n, k = map(int, input().split())

result = bfs(n, k)
print(result)