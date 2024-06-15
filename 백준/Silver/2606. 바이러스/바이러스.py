def dfs(w):
    visited[w] = 1
    for next_com in graph[w]:
        if visited[next_com] == 0:
            dfs(next_com)


n = int(input())
w = int(input())

graph = [[] for i in range(n + 1)]
visited = [0] * (n + 1)

for i in range(w):
    a, b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]

dfs(1)
print(sum(visited) - 1)