def searchMatrix(matrix, target):
    """
    排除法，从左下角或右上角还是查找
    时间复杂度o（m+n）m，n为行列数
    :param matrix:
    :param target:
    :return:
    """
    if not matrix or not matrix[0]:return False
    i,j=len(matrix)-1,0
    while i>=0 and j<len(matrix[i])-1:
        if matrix[i][j]<target:
            j+=1
        elif matrix[i][j]>target:
            i-=1
        else:return True
    return False

matrix=[
  []
]

target=51

print(searchMatrix(matrix,target))