import copy
def solution(n, lost, reserve):
    answer = 0
    y = set(lost) & set(reserve) # 도난 당했지만 여분 옷이 있는 애들 
    losts = set(lost) - y
    reserves = set(reserve) - y
    
    for r in sorted(reserves):
        if r - 1 in losts:   #앞 번호의 학생이 하나를 빌려야 한다면 
            losts.remove(r-1)
        elif r + 1 in losts:  #뒷 번호의 학생이 하나를 빌려야 한다면
        	losts.remove(r+1)
    
    answer = n - len(losts)
    return answer