def solution(board, h, w):
    answer = 0
    dx = [0, 1, -1, 0]
    dy = [1, 0, 0, -1]
    
    for i in range(4):
        if 0 <= h + dx[i] < len(board) and 0 <= w + dy[i] < len(board[0]):
            if board[h][w] == board[h + dx[i]][w + dy[i]]:
                answer += 1
    return answer