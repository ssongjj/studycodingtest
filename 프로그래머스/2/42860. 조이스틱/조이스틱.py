def solution(name):
    answer = 0
    min_move = len(name)-1
    for i, ch in enumerate(name):
        answer += min(ord(ch) - ord('A'), ord('Z')-ord(ch) + 1)
        #A-> ch로 가는 경우와 A -> Z -> ch로 가는 경우 중 최솟값의 경로를 고름 
        
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1
        
        #연속으로 A인 경우의 문자열을 찾아 줌
        
        min_move = min([min_move, 2 * i + len(name) - next, i + 2 * (len(name) - next)])
    
    answer += min_move
        
    return answer