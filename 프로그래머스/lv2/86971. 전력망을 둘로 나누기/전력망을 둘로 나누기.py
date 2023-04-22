from collections import defaultdict

def dfs(v, tree, visited, connected):
    cnt = 1
    visited[v] = True
    
    for vn in tree[v]:
        #해당 송전탑의 방문 이력이 없고 끊어진 간선이 아닌 경우 
        if not visited[vn] and connected[v][vn]:
            cnt += dfs(vn, tree, visited, connected)
    return cnt
    

def solution(n, wires):
    #n개의 송전탑이 트리 형태 
    #node를 방문하면서 끊고 dfs를 통해 각자 연결된 송전탑 수를 가지고 온다
    #송전탑 수의 차이를 비교해서 최솟값을 찾는다
    #dfs라면 재귀 사용
    answer = float('inf')
    tree = defaultdict(list)
    connected = [[True]*(n+1) for _ in range(n+1)] #간선이 끊겼는지 끊기지 않았는지 확인해 주는 리스트
    
    for v1, v2 in wires:
        tree[v1].append(v2) 
        tree[v2].append(v1) 
        #v1과 v2는 연결되어 있으므로 서로 연결시켜 준다.
    for v1, v2 in wires:
        visited = [False] * (n+1)
        connected[v1][v2] = False #간선 연결 끊기
        
        cnt1 = dfs(v1, tree, visited, connected)
        cnt2 = dfs(v2, tree, visited, connected)
        connected[v1][v2] = True #간선 다시 연결해 주기
        
        answer = min(answer, abs(cnt1 - cnt2))
    
    
    return answer