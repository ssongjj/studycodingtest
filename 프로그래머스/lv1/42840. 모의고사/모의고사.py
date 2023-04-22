def solution(answers):
    #OUTPUT: 가장 많은 문제를 맞힌 사람의 리스트
    answer = []
    a_answer = [1, 2, 3, 4, 5] 
    b_answer = [2, 1, 2, 3, 2, 4, 2, 5] 
    c_answer = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0, 0, 0]
    
    for i, ans in enumerate(answers):
        if ans == a_answer[i % len(a_answer)]:
            score[0] += 1
        if ans == b_answer[i % len(b_answer)]:
            score[1] += 1
        if ans == c_answer[i % len(c_answer)]:
            score[2] += 1

    for i, s in enumerate(score):
        if s == max(score):
            answer.append(i+1)
        
    return answer

'''
    first = [1, 2, 3, 4, 5] * len(answers)
    second = [2, 1, 2, 3, 2, 4, 2, 5] * len(answers)
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * len(answers)
    
    s_1 = len(list(i for i, an in enumerate(answers) if an == first[i]))
    s_2 = len(list(i for i, an in enumerate(answers) if an == second[i]))
    s_3 = len(list(i for i, an in enumerate(answers) if an == third[i]))
    
    mx_score = max([s_1, s_2, s_3])
    
    if s_1 == mx_score:
        answer.append(1)
    if s_2 == mx_score:
        answer.append(2)
    if s_3 == mx_score:
        answer.append(3)
    
    
    #for i, a in enumerate(answers):
     #   if a == first[i]:
      #      s_1 += 1
       # if a == second[i]:
        #    s_2 += 1
        #if a == third[i]:
         #   s_3 += 1
'''