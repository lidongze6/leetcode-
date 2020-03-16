def nine_square(n):
    import math
    k = int(math.sqrt(n))
    matrix = [[0 for i in range(k)] for j in range(k)]
    row = k - 1
    col = k // 2
    for i in range(1, n + 1):
        if i != 1:
            if matrix[(row + 1) % k][(col + 1) % k] == 0:
                row, col = (row + 1) % k, (col + 1) % k
            else:
                row, col = (row - 1 + k) % k, col   ## 防止越界的方法，出现负数再加一倍
        matrix[row][col] = i

    for ii in range(k):
        for jj in range(k):
            print(matrix[ii][jj], end=" ")
        print()


nine_square(25)
