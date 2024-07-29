def solution(scores):
    #근무 태도 점수, 동료 평가 점수
    answer = 0
    target = scores[0]
    target_score = sum(scores[0])
    
    scores.sort(key=lambda x: (-x[0], x[1])) # 첫 번째 점수는 내림차순, 두 번째 점수는 오름차순(만약 같다면)
    # 이렇게 하면 [[2,2],[1,4],[3,2],[3,2],[2,1]] -> [[3, 2], [3, 2], [2, 1], [2, 2], [1, 4]]
    max_score = 0 # 가장 높은 평가 점수 
    
    for a, b in scores:
        if target[0] < a and target[1] < b: # 완호보다 두 점수 모두 높은 사원이 한 명이라도 있으면 인센을 받을 수 없음
            return -1
        
        if b >= max_score:
            max_score = b
            if a + b > target_score:
                answer += 1 # 완호보다 점수가 높은 사원 계산
    
    return answer + 1 