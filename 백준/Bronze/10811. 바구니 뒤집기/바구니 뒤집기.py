n, m = map(int, input().split())
answer = list(range(1, n + 1))

for _ in range(m):
    start, end = map(int, input().split())
    answer[start - 1: end] = reversed(answer[start - 1: end])

print(*answer)