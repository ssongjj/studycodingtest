from collections import Counter

def solution(weights):
    answer = 0
    counter = Counter(weights)
    
    # 2 이상인 경우 1:1로 미리 제외해 줌
    for k, v in counter.items():
        if v >= 2:
            answer += v * (v - 1) // 2      # v 개의 항목 중 2 개를 선택하는 경우의 수
            
    weights = set(weights) # 중복 제거
    
    # 나올 수 있는 비율 2:3, 2:4, 3:4
    for weight in weights:
        if weight * 2/3 in weights:
            answer += counter[weight * 2/3] * counter[weight]
        if weight * 1/2 in weights:
            answer += counter[weight * 1/2] * counter[weight]
        if weight * 3/4 in weights:
            answer += counter[weight * 3/4] * counter[weight]
    return answer