
from collections import deque
import sys

input = sys.stdin.readline

def bfs(i):
    visited = [0] * (n + 1)
    queue = deque([i])
    visited[i] = 1
    cnt = 1

    while queue:
        cur = queue.popleft()

        for next_com in com[cur]:
            if not visited[next_com]:
                queue.append(next_com)
                visited[next_com] = 1
                cnt += 1

    return cnt


n, m = map(int, input().split())
com = [[] for _ in range(n + 1)]
answer = []

for _ in range(m):
    a, b = map(int, input().split())
    com[b].append(a)

max_cnt = 0
for i in range(1, n + 1):
    result = bfs(i)
    if max_cnt < result:
        max_cnt = result
        answer.clear()
        answer.append(i)
    elif max_cnt == result:
        answer.append(i)

print(*answer)