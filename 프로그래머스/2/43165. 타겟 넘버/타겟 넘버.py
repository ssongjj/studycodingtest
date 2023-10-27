from itertools import product

def solution(numbers, target):
    l = [(x, -x) for x in numbers]
    s = list(map(sum, product(*l)))
    return s.count(target)

    
'''    
    #순서 바꾸지 않고 적절하게 더하거나 빼서 target 만듦 
    answer = 0
    
    que = [[0, 0]] #[index, 연산값]
    
    while que:
        index, a = que.pop()
        if index < len(numbers):
            que.append([index+1, a+numbers[index]])
            que.append([index+1, a-numbers[index]])

        if index == len(numbers):
            if a == target:
                answer += 1
        
    
    return answer
'''