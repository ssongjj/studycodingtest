def solution(brown, yellow):
    #output: [카펫의 가로, 세로]
    #grid = brown + yellow
    #yellow = (width-2)*(height-2)
    #grid = width * height = brown + (width-2) * (height-2)
    #전체 카펫의 가로의 길이 >= 세로
    answer = []
    grid = brown + yellow
    
    for width in range(grid, 1, -1):
        if grid % width != 0:
            continue
        
        height = grid / width
        y = (width - 2) * (height - 2)
        b = grid - y
        
        if y == yellow and b == brown and width >= height:
            answer.append(width)
            answer.append(height)
    
    return answer