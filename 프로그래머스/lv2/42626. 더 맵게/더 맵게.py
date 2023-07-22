import heapq

def solution(scoville, K):
    answer = 0
    scoville.sort()
    heapq.heapify(scoville)
    
    if all(K <= score for score in scoville):
        return 0
    
    while(scoville):
        if len(scoville) <= 1:
            if heapq.heappop(scoville) < K:
                return -1
            else:
                return answer
            
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        
        if a < K:
            heapq.heappush(scoville, a + (b * 2))
            answer += 1
        else:
            break
    
    return answer