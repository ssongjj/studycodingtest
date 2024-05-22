def solution(rows, columns, queries):
    answer = []
    matrix = []

    for y in range(rows):
        matrix.append([i for i in range(y * columns + 1, (y + 1) * columns + 1)])

    for q in queries:
        q = [x - 1 for x in q]
        x1, y1, x2, y2 = q
        tmp = matrix[x1][y1]
        small = tmp

        for i in range(x1 + 1, x2 + 1):
            matrix[i - 1][y1] = matrix[i][y1]
            small = min(small, matrix[i][y1])

        for i in range(y1 + 1, y2 + 1):
            matrix[x2][i - 1] = matrix[x2][i]
            small = min(small, matrix[x2][i])

        for i in range(x2 - 1, x1 - 1, -1):
            matrix[i + 1][y2] = matrix[i][y2]
            small = min(small, matrix[i][y2])

        for i in range(y2 - 1, y1 - 1, -1):
            matrix[x1][i + 1] = matrix[x1][i]
            small = min(small, matrix[x1][i])
        
        matrix[x1][y1 + 1] = tmp

        answer.append(small)

    return answer