def rotation_matrix(matrix):
    """
    空间复杂度o(1) 实现顺时针旋转90°
    """
    l = len(matrix)
    layer = len(matrix) // 2
    for i in range(layer):
        for j in range(i, l - i - 1):
            tmp = matrix[i][j]
            # left-->top
            matrix[i][j] = matrix[l - j - 1][i]  # top:行不变，列滑动，故行为i，列为j
            # bottom-->left
            matrix[l - j - 1][i] = matrix[l - i - 1][l - j - 1]  # left:列不变，行滑动，故列为i，行为j
            # right-->bottom
            matrix[l - i - 1][l - j - 1] = matrix[j][l - i - 1]  # bottom:行不变，列滑动，故行位i，列为j
            # top-->right
            matrix[j][l - i - 1] = tmp  # right:列不变，行滑动，故列为i，行为j

    for ii in range(l):
        for jj in range(l):
            print(matrix[ii][jj], end=" ")
        print("\n")


matrix = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14], [15, 16, 17, 17, 19], [20, 21, 22, 23, 24]]
l = len(matrix)
for ii in range(l):
    for jj in range(l):
        print(matrix[ii][jj], end=" ")
    print("\n")
print("------------\n")

rotation_matrix(matrix)
