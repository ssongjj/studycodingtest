def solution(clothes):  
    answer = 1
    c_dicts = {key: [] for _, key in clothes}
    
    for v, k in clothes:
        c_dicts[k].append(v)
        
    for k, v in c_dicts.items():
        answer *= len(c_dicts[k]) + 1

    return answer - 1 











    '''
    answer = 1
    dict = {key:[] for _,key in clothes}
    
    for v, k in clothes:
        dict[k].append(v)
    
    if len(dict.keys()) == 1:
        answer = len(clothes)
        return answer
    
    for values in dict.values():
        answer *= (len(values) + 1)
    # +1을 해 주는 이유: 입지 않는 경우도 포함    
    return answer - 1 
    # 둘 다 입지 않는 경우의 수가 존재하기 때문에 총 경우의 수에서 -1 처리해 줌
    
    
    answer = 1
    dict = {key: [] for _, key in clothes}
    
    for v, k in clothes:
        dict[k].append(v)
        
    if len(dict.keys()) == 1:
        answer = len(clothes)
        return answer
    
    for values in dict.values():
        answer *= (len(values) + 1)
    
    return answer - 1

    '''