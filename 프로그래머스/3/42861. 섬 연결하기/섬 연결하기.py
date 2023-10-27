def solution(n, costs):
    #[a, b, c] a와 b는 연결되어 있고 c는 비용
    # 최소 cost를 찾아야 함으로 크루스칼 알고리즘
    answer = 0
    parent = [0] * (n + 1)
    for i in range(1, n+1):
        parent[i] = i
        
    costs.sort(key = lambda x: x[2])
    
    def find_parent(x):
        if parent[x] != x:
            parent[x] = find_parent(parent[x])
        else:
            return x
        return parent[x]
    
    def union_parent(x, y):
        a = find_parent(x)
        b = find_parent(y)
        
        if a < b:
            parent[b] = a
        else:
            parent[a] = b
            
    
    for i, j, cost in costs:
        if find_parent(i) != find_parent(j):
            union_parent(i, j)
            answer += cost
            
    return answer


'''
    parent = [0] * (n+1)
    for i in range(1, n+1):
        parent[i] = i 
    #cost가 낮은 순으로 sort
    costs.sort(key = lambda x: x[2])
    
    #정렬된 간선 정보를 하나씩 확인하면서 사이클을 발생시키는지 확인
    #사이클이 발생하지 않으면 최소 신장 트리에 포함
    def find_parent(x):
        if parent[x] != x:
            parent[x] = find_parent(parent[x])
        else:
            return x
        return parent[x]
    
    def union_parent(a, b):
        a = find_parent(a)
        b = find_parent(b)
        
        if a < b:
            parent[b] = a
        else:
            parent[a] = b
            
    for n1, n2, cost in costs:
        if find_parent(n1) != find_parent(n2):
            print(find_parent(n1), find_parent(n2))
            union_parent(n1, n2)
            print(find_parent(n1), find_parent(n2))
            answer += cost
'''
