#한 심사대는 동시에 한 명만 심사 가능
#모든 사람들이 심사를 받는데 걸리는 시간을 "최소"로
#제일 짧은 시간이 걸리는 심사대가 많은 심사를 해야 함.

#걸리는 시간의 최대와 시간의 최소를 구하고 중간 값이 n명을 심사할 수 있는지 없는지 확인
def solution(n, times):
    answer = 0
    times.sort()
    
    left = min(times)
    right = max(times)*n #걸리는 시간의 최대한 제일 오래 걸리는 심사관에서 모두 검사를 받는 경우
    
    while left <= right:
        mid = (left + right)//2
        c = 0
        
        for time in times:
            c += mid // time #c는 중간 시간 동안 각 심사관이 심사한 사람의 수
            #최소 시간이 걸리는 심사위원부터 심사를 하기 때문에 모든 심사관을 거치지 않아도 mid분 동안 n명의 심사를 할 수 있다면 종료
            if c >= n:
                break
        
        if c >= n: #심사한 사람의 수가 심사받을 사람보다 많거나 같다 (최댓값 이동 필요) -> 시간이 남음
            answer = mid  
            right = mid - 1
        else: #심사한 사람 수가 심사받을 사람 수보다 적다 (최소값 이동 필요) -> 시간이 더 필요 
            left = mid + 1 

            
    return answer