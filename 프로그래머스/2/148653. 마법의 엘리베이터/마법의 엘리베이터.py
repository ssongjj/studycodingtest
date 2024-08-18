def solution(storey):
    answer = 0
    
    while storey > 0:
        cur = storey % 10
        nx = (storey // 10) % 10
        
        # 현재 자릿수가 5 이상이면, 10에서 빼는 것이 유리함
        if cur > 5 or (cur == 5 and nx >= 5):
            answer += 10 - cur
            storey += 10  # 올림 처리
        else:
            answer += cur
        
        # 한 자릿수 아래로 이동
        storey //= 10
    
    return answer