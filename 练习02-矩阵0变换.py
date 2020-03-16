def zeros(matrix):
    m = len(matrix) * [None]
    n = len(matrix[0]) * [None]
    for i in range(len(m)):
        for j in range(len(n)):
            if matrix[i][j] == 0:
                m[i], n[j] = 1, 1

    for i in range(len(m)):
        for j in range(len(n)):
            if m[i] == 1 or n[j] == 1:
                matrix[i][j] = 0
