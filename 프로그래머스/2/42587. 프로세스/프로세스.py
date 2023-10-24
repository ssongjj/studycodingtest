from collections import deque

def solution(priorities, location):
    #중요도
    #하나를 먼저 꺼낸 뒤 중요도가 하나라도 더 높은 게 있으면 J를 꺼내서 다시 뒤로
    #그렇지 않으면 J를 꺼낸다
    answer = 0
    p_list = [(p, i) for i, p in enumerate(priorities)]
    queue = deque(p_list)
    
    while queue:
        process = queue.popleft()
        
        if any(process[0] < q[0] for q in queue):
            queue.append(process)
        else:
            answer += 1
            if process[1] == location:
                break
    
    return answer

'''
    answer = 0
    lst = [(p, i) for i, p in enumerate(priorities)]
    deq = deque(lst)
    
    while(deq):
        #y의 값이 location이랑 일치하는데 빠지는 경우 cnt를 answer로 return
        tmp = deq.popleft()
        #any는 () 안의 식이 하나라도 true면 true, all은 모두 true여야 true
        if any(tmp[0] < q[0] for q in deq):
            deq.append(tmp)           
        else:
            answer += 1
            if location == tmp[1]:
                return answer
'''