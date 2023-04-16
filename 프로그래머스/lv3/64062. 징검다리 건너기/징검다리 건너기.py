def solution(stones, k):
    #범위가 매우 크다 -> 이분 탐색
    #이 문제는 결정 문제로 바꿀 수 있기 때문에 파라메트릭 서치도 가능하다
    #어떻게 바꿀 것인가? k명의 사람이 징검다리를 건널 수 있는가 -> True False
    
    #이분탐색
    answer = 0    
    left, right = min(stones), max(stones)

    while left <= right:
        cnt = 0
        mid = (left + right) //2
        
        for stone in stones:
            if stone - mid <= 0:
                cnt += 1   #뺀 값이 0보다 작으면 건널 수 없는 경우이기 때문에 cnt+1을 해 준다
                if cnt >= k: #다만 cnt가 k와 같아지거나 커질 경우 디딤돌을 mid명이 건널 수 없기 때문에 right값 조정
                    right = mid - 1
                    break
            else:
                cnt = 0   #이 경우는 건널 수 있기 때문에 cnt를 0으로 초기화해 준다.
        else: #for문을 다 돌았다면 mid명이 디딤돌을 건넌 것임으로 left 값을 조정해 준다.
            left = mid + 1
    
    answer = left
        
    return answer