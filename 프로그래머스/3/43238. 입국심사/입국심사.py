#한 심사대는 동시에 한 명만 심사 가능
#모든 사람들이 심사를 받는데 걸리는 시간을 "최소"로
#제일 짧은 시간이 걸리는 심사대가 많은 심사를 해야 함.

#걸리는 시간의 최대와 시간의 최소를 구하고 중간 값이 n명을 심사할 수 있는지 없는지 확인
def solution(n, times):
    answer = 0
    times.sort()
    
    left = min(times)
    right = max(times) * n
    
    while left <= right:
        mid = (left + right) // 2
        c = 0
        
        for time in times:
            c += mid // time
            if c >= n:
                break
        
        if c >= n: 
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
            
    return answer