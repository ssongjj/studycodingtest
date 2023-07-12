from collections import Counter

def solution(X, Y):
    answer = ''
    
    x_counter = Counter(X)
    y_counter = Counter(Y)
    
    for i in range(9, -1, -1):
        if str(i) in x_counter and str(i) in y_counter:
            min_common = min(x_counter[str(i)], y_counter[str(i)])
            answer += str(i) * min_common
    
    if answer == "":
        answer = "-1"
    
    if answer[0] == "0":
        answer = "0"
            
    return answer