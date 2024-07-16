from sys import stdin
from collections import deque


def bfs(s, t):
    queue = deque()
    queue.append((s, t, 0))  # s, t, cnt

    while queue:
        hit, hurt, cnt = queue.popleft()
        if hit <= hurt:
            queue.append((hit * 2, hurt + 3, cnt + 1))
            queue.append((hit + 1, hurt, cnt + 1))

            if hit == hurt:
                return cnt


input = stdin.readline
c = int(input())
for _ in range(c):
    s, t = map(int, input().split())
    print(bfs(s, t))