from collections import deque 

def solution(prices):
    que = deque(prices)
    answer = []
    
    while(que):
        price = que.popleft()
        cnt = 0
        for i in que:
            if price > i:
                cnt += 1
                break
            else:
                cnt+= 1
        answer.append(cnt)
    return answer