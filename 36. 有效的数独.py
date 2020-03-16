def isValidSudoku(matrix) -> bool:
    for i in range(len(matrix)):
        col_s = set()
        row_s = set()
        max_s = set()
        for j in range(len(matrix[i])):
            if matrix[i][j] != ".":
                if matrix[i][j] in col_s:
                    return False
                else:
                    col_s.add(matrix[i][j])

            if matrix[j][i] != ".":
                if matrix[j][i] in row_s:
                    return False
                else:
                    row_s.add(matrix[j][i])

            idx = (i // 3) * 3 + j // 3
            idy = (i % 3) * 3 + j % 3
            if matrix[idx][idy] != ".":
                if matrix[idx][idy] in max_s:
                    return False
                else:
                    max_s.add(matrix[idx][idy])
        col_s.clear()
        row_s.clear()
        max_s.clear()
    return True