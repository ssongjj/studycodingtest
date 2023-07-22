from collections import defaultdict
from collections import deque

def solution(record):
    answer = []
    userid_dict = defaultdict(str)
    
    queue = deque(record)
    
    while queue:
        re = queue.popleft().split(" ")
        comm = re[0]
        
        if comm == "Enter":
            comm, userid, usernm = re
            userid_dict[userid] = usernm
            answer.append('{}님이 들어왔습니다.'.format(userid))
        elif comm == "Leave":
            comm, userid = re
            usernm = userid_dict[userid]
            answer.append('{}님이 나갔습니다.'.format(userid))
        else:
            comm, userid, usernm = re
            userid_dict[userid] = usernm
            
    n_answer = []
    for s in answer:
        userid = s.split("님")[0]
        n_answer.append(s.replace(userid, userid_dict[userid]))
    
    return n_answer