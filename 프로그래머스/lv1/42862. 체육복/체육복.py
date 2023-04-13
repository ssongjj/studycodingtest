import copy
def solution(n, lost, reserve):
    #바로 앞번호 학생이나 뒷번호 학생에게만 체육복을 빌려줄 수 있음 
    #최대한 많은 학생이 수업을 들어야 함
    s = set(lost) & set(reserve)    #lost와 reserve의 교집합을 구한다. 이 교집합이 본인의 것을 이미 하나 소지하고 있어서 확인할 필요 없는 학생들
    l = set(lost) - s     			#체육복을 빌려야 하는 친구들 
    r = set(reserve) - s			#여분은 가지고 왔으나 도난 당하지는 않아서 빌려줄 수 있는 학생들
    
    for x in sorted(r):
        if x - 1 in l:   #앞 번호의 학생이 하나를 빌려야 한다면 
            l.remove(x-1)
        elif x + 1 in l:  #뒷 번호의 학생이 하나를 빌려야 한다면
        	l.remove(x+1)
    #이 순환문이 끝나면 l에 남아 있는 학생들은 빌리지 못한 학생들이기 때문에
    
    return n - len(l)