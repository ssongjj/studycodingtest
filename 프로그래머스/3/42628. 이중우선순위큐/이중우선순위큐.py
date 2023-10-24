import heapq

def solution(operations):
    minheap = []
    heapq.heapify(minheap)
    
    for i in operations:
        comm, num = i.split(' ')
        
        if comm == 'I': #I면 무조건 힙에 넣어 줌
            heapq.heappush(minheap, int(num))
        else:
            if len(minheap) > 0: #minheap이 0보다 클 때 0보다 작으면 최댓값과 최솟값을 뽑는 것이 의미가 없어서
                if num == '1':
                    minheap.pop(minheap.index(heapq.nlargest(1, minheap)[0]))
                else:
                    heapq.heappop(minheap)
                
    if len(minheap) == 0:
        return [0, 0]
    else:
        answer = [heapq.nlargest(1, minheap)[0], heapq.heappop(minheap)]
                
    
    return answer