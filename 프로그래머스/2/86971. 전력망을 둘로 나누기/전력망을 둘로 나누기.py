from collections import defaultdict, deque

def BFS(n, startNode, tree, connections):
    cnt = 1
    queue = deque([startNode])
    visited = [False for _ in range(n+1)]
    
    while queue:
        node = queue.popleft()
        visited[node] = True 
        
        for next_node in tree[node]:
            if connections[node][next_node] and connections[next_node][node] and not visited[next_node]:
                visited[next_node] = True
                queue.append(next_node)
                cnt += 1

    return cnt

def solution(n, wires):
    answer = n 
    tree = defaultdict(list)
    connections = [[False for _ in range(n+1)] for _ in range(n+1)]
    
    for wire in wires:
        tree[wire[0]].append(wire[1])
        tree[wire[1]].append(wire[0])
        connections[wire[0]][wire[1]] = True
        connections[wire[1]][wire[0]] = True
        
    for wire in wires:
        # 연결 끊기 
        connections[wire[0]][wire[1]] = False
        connections[wire[1]][wire[0]] = False
        answer = min(answer, abs(BFS(n, wire[0], tree, connections) - BFS(n, wire[1], tree, connections)))
        
        # 다시 붙이기
        connections[wire[0]][wire[1]] = True
        connections[wire[1]][wire[0]] = True

    return answer


'''union-find
uf = []

def find(a):
    global uf
    if uf[a] < 0: return a
    uf[a] = find(uf[a])
    return uf[a]

def merge(a, b):
    global uf
    pa = find(a)
    pb = find(b)
    if pa == pb: return
    uf[pa] += uf[pb]
    uf[pb] = pa

def solution(n, wires):
    global uf
    answer = int(1e9)
    k = len(wires)
    for i in range(k):
        uf = [-1 for _ in range(n+1)]
        tmp = [wires[x] for x in range(k) if x != i]
        for a, b in tmp: merge(a, b)
        v = [x for x in uf[1:] if x < 0]
        answer = min(answer, abs(v[0]-v[1]))
'''