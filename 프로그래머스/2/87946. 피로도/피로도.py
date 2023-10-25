from itertools import permutations

def solution(k, dungeons):
    answer = 0
    #최소 필요 필요도: 가지고 있어야 하는 최소한의 필요도
    #소모 피로도: 소모되는 필요도
    for dungeon in permutations(dungeons, len(dungeons)):
        tmp_k = k
        cnt = 0
        
        for min_p, use_p in dungeon:
            if tmp_k >= min_p:
                cnt += 1
                tmp_k -= use_p
        answer = max(cnt, answer)
        
    return answer