import copy 

def solution(people, limit):
    #구명보트는 최대 2 명씩만 탈 수 있음 
    #구명보트를 최대한 적게 사용해서 모든 사람이 탈출
    answer = 0
    people.sort()
    
    start = 0
    end = len(people) - 1
    
    while start <= end:
        if people[start] + people[end] > limit:
            answer += 1
            end -= 1
        else:
            answer += 1
            start += 1
            end -= 1
    
    return answer
    
    