def searchMatrix(matrix, target):
    l=len(matrix)
    for _ in range(l):
        left,right=0,len(matrix[_])-1
        if right<0:return False
        while left<right:
            mid=(left+right)//2
            if matrix[_][mid]==target:
                return True
            elif matrix[_][mid]>target:right=mid-1
            elif matrix[_][mid]<target:left=mid+1
        if left>=right:
            if matrix[_][left] == target:
                return True
    return False


matrix=[
  []
]

target=30
print(searchMatrix(matrix,target))
