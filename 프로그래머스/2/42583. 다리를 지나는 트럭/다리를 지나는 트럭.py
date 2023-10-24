from collections import deque

def solution(bridge_length, weight, truck_weights):
    # 모든 트럭이 다리를 건널 때 걸리는 최소 시간 (초)
    answer = 0
    wait_q = deque(truck_weights)
    move_q = deque()
    
    while wait_q or move_q:
        answer += 1
        
        if move_q and move_q[0][1] == bridge_length:
            move_q.popleft()
        
        if wait_q and sum(t[0] for t in move_q) + wait_q[0] <= weight:
            truck = wait_q.popleft()
            move_q.append([truck, 0]) # weight, cnt
            
        for t in move_q:
            t[1] += 1

    return answer