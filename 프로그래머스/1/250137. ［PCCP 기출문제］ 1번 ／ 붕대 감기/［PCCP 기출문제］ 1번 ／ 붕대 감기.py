def solution(bandage, health, attacks):
    answer = health
    att_prev = 0
    t, x, y = bandage
    
    for i in range(len(attacks)):
        att, dmg = attacks[i]
        if i > 0:
            att_prev = attacks[i-1][0]

        add = att - att_prev - 1
        
        answer += add * x
        if add >= t:
            answer += y * (add // t)
        if answer > health:
            answer = health
        
        answer -= dmg
        
        print(answer)
        
        if answer <= 0:
            return -1
    
    return answer