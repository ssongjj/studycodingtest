def solution(rows, columns, queries):
    answer = []
    matrix = []

    for y in range(rows):
        matrix.append([i for i in range(y * columns + 1, (y + 1) * columns + 1)])

    for q in queries:
        q = [x - 1 for x in q]
        y1, x1, y2, x2 = q
        tmp = matrix[y1][x1]
        small = tmp

        for i in range(y1 + 1, y2 + 1):
            matrix[i - 1][x1] = matrix[i][x1]
            small = min(small, matrix[i][x1])

        for i in range(x1 + 1, x2 + 1):
            matrix[y2][i - 1] = matrix[y2][i]
            small = min(small, matrix[y2][i])

        for i in range(y2 - 1, y1 - 1, -1):
            matrix[i + 1][x2] = matrix[i][x2]
            small = min(small, matrix[i][x2])

        for i in range(x2 - 1, x1 - 1, -1):
            matrix[y1][i + 1] = matrix[y1][i]
            small = min(small, matrix[y1][i])
        
        matrix[y1][x1 + 1] = tmp

        answer.append(small)

    return answer