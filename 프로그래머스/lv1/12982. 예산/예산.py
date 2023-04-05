#전체 예산이 정해져 있음 -> 최대한 많은 부서의 물품을 구매
#물품을 구매할 때는 일부만 줄 수 없고 신청한 금액 모두를 줘야 함
def solution(d, budget):
    answer = 0
    d.sort()
    
    #1 sort 후 작은 수부터 budget에서 빼 주고 만약 다음 부서의 예산이 남은 budget보다 클 경우 종료
    '''
    for n in d:
        if budget - n < 0:
            break 
        budget -= n
        answer += 1 
    
    return answer
    '''
    
    #2 sort 후 d의 합이 budget보다 크면 제일 부서 예산이 큰 곳부터 제거 후 남는 부서를 계산
    while budget < sum(d):
        d.pop()
    
    return len(d)