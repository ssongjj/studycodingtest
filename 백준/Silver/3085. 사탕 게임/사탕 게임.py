def count_candies(board):
    result = 0

    for i in range(n):
        for j in range(n - 1):
            if board[i][j] != board[i][j + 1]:
                board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]
                result = max(result, get_count(board))
                board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]

    for i in range(n):
        for j in range(n - 1):
            if board[j][i] != board[j + 1][i]:
                board[j][i], board[j + 1][i] = board[j + 1][i], board[j][i]
                result = max(result, get_count(board))
                board[j][i], board[j + 1][i] = board[j + 1][i], board[j][i]

    return result


def get_count(board):
    result = 0

    for i in range(n):
        cnt = 1
        for j in range(1, n):
            if board[i][j] == board[i][j - 1]:
                cnt += 1
            else:
                cnt = 1
            result = max(result, cnt)

    for i in range(n):
        cnt = 1
        for j in range(1, n):
            if board[j][i] == board[j - 1][i]:
                cnt += 1
            else:
                cnt = 1
            result = max(result, cnt)

    return result


n = int(input())
board = [list(input()) for _ in range(n)]

print(count_candies(board))