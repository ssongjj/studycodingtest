import collections 

def solution(participant, completion):
    p_counter = collections.Counter(participant)
    c_counter = collections.Counter(completion)
    
    # 카운터끼리는 빼기가 가능하다
    nc_counter = p_counter - c_counter
    answer = ''.join(nc_counter.keys())
    return answer