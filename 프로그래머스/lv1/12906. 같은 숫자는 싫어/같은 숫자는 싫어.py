def solution(arr):
    answer =['inf']
    
    for i in arr:
        if answer[-1] != i:
            answer.append(i)

    answer.pop(0)
    return answer
