from itertools import product

def solution(word):
    w = ['A', 'E', 'I', 'O', 'U']
    p_list = []
    
    for i in range(1, len(w)+1):
        p_list.extend(map(''.join, list(product(w, repeat = i))))
        
    p_list.sort()
    return p_list.index(word) + 1