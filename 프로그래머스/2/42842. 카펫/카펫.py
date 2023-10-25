def solution(brown, yellow):
    grid = brown + yellow
    answer = []
    
    for w in range(grid, 1, -1):
        if grid % w != 0:
            continue
            
        h = grid / w
        y = (w - 2) * (h - 2)
        b = grid - y
        
        if b == brown and y == yellow:
            return [w, h]
    return answer
    
    '''
    #output: [카펫의 가로, 세로]
    #grid = brown + yellow
    #yellow = (width-2)*(height-2)
    #grid = width * height = brown + (width-2) * (height-2)
    #전체 카펫의 가로의 길이 >= 세로
    answer = []
    grid = brown + yellow
    
    for width in range(grid, 1, -1):
        #width를 임의로 설정해서 만약 grid = width * height가 될 수 없을 때는 다음으로 넘어간다.
        if grid % width != 0:  
            continue
        
        height = grid / width
        y = (width - 2) * (height - 2)
        b = grid - y
        
        if y == yellow and b == brown and width >= height: 
            answer.append(width)
            answer.append(height)
    '''       
    
    return answer