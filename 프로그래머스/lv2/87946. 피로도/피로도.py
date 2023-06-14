from itertools import permutations #순열

def solution(k, dungeons):
    answer = 0
    #최소 필요 필요도: 가지고 있어야 하는 최소한의 필요도
    #소모 피로도: 소모되는 필요도
    
    for dungen in permutations(dungeons, len(dungeons)):
        cal_k = k
        cnt = 0
        
        for i in dungen:
            if i[0] <= cal_k:
                if cal_k - i[1] <= 0:
                    break
                else:
                    cal_k -= i[1]
                    cnt += 1
        answer = max(answer, cnt)
    
    return answer