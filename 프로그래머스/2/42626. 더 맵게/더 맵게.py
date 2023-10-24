import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    
    cnt = 0
    
    
    while len(scoville) >= 2:
        if scoville[0] >= K:
            return cnt
        
        min1 = heapq.heappop(scoville)	
        min2 = heapq.heappop(scoville)
        heapq.heappush(scoville, min1 + min2 * 2) 
        cnt += 1
        
    if scoville[0] >= K:
        return cnt

    return -1