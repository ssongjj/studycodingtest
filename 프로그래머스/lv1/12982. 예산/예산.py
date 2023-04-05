#전체 예산이 정해져 있음 -> 최대한 많은 부서의 물품을 구매
#물품을 구매할 때는 일부만 줄 수 없고 신청한 금액 모두를 줘야 함
#sort 후 작은 수부터 budget에서 빼 주고 만약 다음 부서의 예산이 남은 budget보다 클 경우 종료
def solution(d, budget):
    answer = 0
    d.sort()
    
    for n in d:
        if budget - n < 0:
            break 
        budget -= n
        answer += 1
        
    return answer