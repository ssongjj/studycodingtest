def solution(s):
    answer = ''
    l = s.split(" ")
    a_lst = []
    for ch in l:
        st = ""
        for i, c in enumerate(ch):
            if i%2 != 0:
                st += c.lower()
            else:
                st += c.upper()
        a_lst.append(st)
    answer = ' '.join(a_lst)
    
    
    return answer