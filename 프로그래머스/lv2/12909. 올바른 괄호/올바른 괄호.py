from collections import deque

def solution(s):
    answer = True
    #()가 전환될 때 (의 수와 )수가 동일한지 파악해야 함
    #)로 시작할 경우 볼 것도 없이 false 처리
    '''
    lst = list(map(str, s))
    if lst[0] == ')':
        return False
    
    cnt = 0

    while len(lst) > 0:
        if lst[0] == '(':
            cnt += 1
        else:
            cnt -= 1
            
        if cnt < 0:
            answer = False
            break
        lst.pop(0)
        
    
    if cnt > 0:
        return False
    '''
    cnt = 0
    que =deque(s) 
    while len(que) > 0:
        gawlho = que.popleft() 
        if gawlho == "(" :
            cnt+=1
        else : 
            cnt-=1
        if cnt < 0 :
            answer = False
            break 
    if cnt > 0 : 
        answer = False
    
    return answer