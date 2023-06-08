def solution(tickets):
    routes = {}
    for t in tickets:
        routes[t[0]] = routes.get(t[0], []) + [t[1]]
    for r in routes:
        routes[r].sort(reverse=True) #알파벳 순서의 역순으로
        
    stack = ["ICN"] #어차피 무조건 시작은 인천 공항
    path = []
    
    while stack:
        top = stack[-1]
        if top not in routes or len(routes[top]) == 0: #어떤 공항에서 출발하는 표가 없거나 표는 있었는데 없게 된다면
            path.append(stack.pop())
        else:
            stack.append(routes[top][-1])
            routes[top] = routes[top][:-1]
    
    return path[::-1] #역순으로 출력