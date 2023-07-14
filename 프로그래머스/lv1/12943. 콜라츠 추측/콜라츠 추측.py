def solution(num):
    answer = 0
    
    for i in range(0, 500):
        if num == 1:
            answer = i 
            break
        
        if num % 2 == 0:
            num = num / 2
        else:
            num = num * 3 + 1
    else:
        answer = -1
            
    
    return answer