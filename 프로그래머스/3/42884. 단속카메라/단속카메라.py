def solution(routes):
    answer = 1
    # 모든 차량이 단속용 카메라는 한 번은 만날 수 있게 적어도 
    routes.sort(key = lambda x: x[0])
    
    s = -float('inf')
    e = 0
    for start, end in routes:
        s = max(s, start)
        e = min(e, end)
        
        if e - s >= 0:
            continue
        else:
            s = start 
            e = end
            answer += 1 
    return answer