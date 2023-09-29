def solution(survey, choices):
    answer = ''
    type = {"R" : 0,"T" : 0,"C" : 0,"F" : 0,"J" : 0,"M" : 0,"A" : 0,"N" : 0 }
    
    for s,c in zip(survey,choices):
        if c > 4:
            type[s[1]] += c - 4
        else:
            type[s[0]] += 4 - c
            
    type_list = list(type.items())
    
    for i in range(0, 8, 2):
        if type_list[i][1] < type_list[i+1][1]:
            answer += type_list[i+1][0]
        else:
            answer += type_list[i][0]
                
    return answer