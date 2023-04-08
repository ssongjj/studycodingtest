# n개를 제거한 후 각 지점의 거리 최솟값 중 가장 큰 값 -> 이해하고 싶다
# 돌 사이의 거리가 짧은 애들이 빠져야 함
# 최소 범위에 들어가는 값들이 있는데 그중 최댓값을 구하라는 것
def solution(distance, rocks, n):
    answer = 0
    left, right = 1, distance 
    
    rocks.sort() #징검다리 정렬 
    
    #이분 탐색
    while left <= right:
        mid = (left + right)//2
        del_st = 0 #제거한 돌을 카운트하기 위한 변수
        pre_st = 0 #기준이 되는 돌
        
        for rock in rocks:
            #돌 사이의 거리가 mid보다 작으면 돌 하나를 제거한다 
            if rock - pre_st < mid:  
                del_st += 1 
            #그게 아니라면 기준 돌을 밟고 건너기 때문에 다음 돌로 이동해 준다
            else:
                pre_st = rock
            
            # 문제에서 요구하는 제거할 바위 n개보다 더 많은 돌이 제거될 필요가 없음
            if del_st > n:
                break
                
        #만약 제거된 돌이 많으면 최댓값이 줄어야 함 (거리가 줄어야 됨)
        if del_st > n:
            right = mid - 1
        #제거된 돌이 적거나 동일하면 최솟값이 늘어야 함 
        else:
            answer = mid
            left = mid + 1
                
    
    return answer