from itertools import combinations_with_replacement

def diff_score(apeach, lion):
    apeach_score = 0
    lion_score = 0
    
    for i in range(10, 0, -1):
        if apeach[10 - i] == 0 and lion[10 - i] == 0:
            continue
        if apeach[10 - i] >= lion[10 - i]:
            apeach_score += i
        else:
            lion_score += i
    return lion_score - apeach_score

def solution(n, info):
    # 큰 점수 차이라면 최대 점수를 구해야 한다
    # 최대 점수가 여러 가지가 나올 수 있다면 낮은 점수를 많이 맞춘 경우를 출력한다 
    answer = [-1]
    max_score = 0
    
    for case in list(combinations_with_replacement(range(11), r = n)):
        lion = [0] * 11
        for e in case:
            lion[10 - e] += 1
        
        cur_score = diff_score(info, lion)
        if max_score < cur_score:
            max_score = cur_score
            answer = lion
            
    return answer