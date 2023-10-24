import math
from collections import deque

def solution(progresses, speeds):
    answer = []
    
    days = [ math.ceil((100 - p)/s) for p, s in zip(progresses, speeds)]
    
    cnt = 1
    queue = deque(days)
    
    day = queue.popleft()
    while queue:
        n_day = queue.popleft()
        if day >= n_day:
            cnt += 1
        else:
            answer.append(cnt)
            day = n_day
            cnt = 1
    answer.append(cnt)
    return answer

'''
    #뒤에 있는 기능이 먼저 개발되어도 앞에 있는 기능이 배포될 때 같이 배포된다
    #배포는 하루에 한 번만 가능
    
    day = [ math.ceil((100-i)/v) for i, v in zip(progresses, speeds)]
    
    cnt = 0
    p = day[0]
    for i in range(len(day)):
        if p < day[i]:
            answer.append(cnt)
            p = day[i]
            cnt = 0
        cnt += 1
    else:
        answer.append(cnt)
'''