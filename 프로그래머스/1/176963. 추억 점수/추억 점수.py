from collections import defaultdict

from collections import defaultdict

def solution(name, yearning, photo):
    answer = []
    yearnig_dict = defaultdict(int)
    
    for n, y in zip(name, yearning):
        yearnig_dict[n] = y

    return [sum(yearnig_dict[n] for n in n_list) for n_list in photo]

'''
def solution(name, yearning, photo):
    answer = []
    yearnig_dict = defaultdict(int)
    
    for n, y in zip(name, yearning):
        yearnig_dict[n] = y
    
    for n_list in photo:
        score = 0
        for n in n_list:
            score += yearnig_dict[n]
        answer.append(score)
            
    return answer
'''