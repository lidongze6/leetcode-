def kthSmallest(matrix, k):
    row = len(matrix)
    col = len(matrix[0])
    left = matrix[0][0]
    right = matrix[row - 1][col - 1]
    while left < right:
        mid = (left + right) // 2
        count = counter(matrix, mid)  # 得到count个小于等于mid的数
        if count < k:
            left = mid + 1
        elif count >= k:
            right = mid

    return right


def counter(matrix, target):
    """
    寻找小于等于target的元素个数
    """
    couter = 0
    row = len(matrix)
    col = len(matrix[0])
    j = col - 1
    while j >= 0:
        i = 0
        while i < row:
            if matrix[i][j] > target:
                couter += row - i
                break
            else:
                i += 1
        j -= 1
    return row * col - couter


matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
k = 8
print(kthSmallest(matrix, k))
