board = list(input().split('.'))
new_board = ''

for b in board:
    if len(b) % 2 != 0:
        print(-1)
        break
    while len(b) >= 4:
        new_board += 'AAAA'
        b = b[4:]
    if len(b) % 2 == 0:
        new_board += 'BB' * (len(b) // 2)
    new_board += '.'
else:
    print(new_board[:-1])