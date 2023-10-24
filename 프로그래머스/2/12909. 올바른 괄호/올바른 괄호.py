from collections import deque

def solution(s):
    answer = True
    cnt = 0
    
    queue = deque(s)
    while queue:
        gawlho = queue.popleft()
        if gawlho == "(":
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
            return False
    if cnt > 0:
        return False
    
    return answer