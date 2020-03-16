def searchMatrix(matrix, target):
    if not matrix:return False
    l1,r1=0,len(matrix)-1
    while l1<r1:
        mid=l1+(r1-l1+1)//2
        if matrix[mid][0]<=target:
            l1=mid
        else:r1=mid-1
    if l1>=r1:
        row=l1

    l2,r2=0,len(matrix[row])-1
    while l2<=r2:
        mid=l2+(r2-l2+1)//2
        if matrix[row][mid]==target:return True
        elif matrix[row][mid]>target:
            r2=mid-1
        else:
            l2=mid+1
    return False


matrix = [[]

]
target = 23

print(searchMatrix(matrix,target))