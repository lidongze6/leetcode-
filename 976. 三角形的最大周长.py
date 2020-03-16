def largestPerimeter(A):
    """
    选择排序，依次找到最大的三个数，判断能否组成三角形
    """
    if len(A) <= 2: return 0
    l = len(A)

    A=mergesort(A)
    m = 0
    while m <= l - 3:
        if A[m] < A[m + 1] + A[m + 2]:
            return A[m] + A[m + 1] + A[m + 2]
        else:
            m += 1
    return 0

def mergesort(A):
    if len(A)==1:
        return A
    mid=len(A)//2
    left=mergesort(A[:mid])
    right=mergesort(A[mid:])
    return merge(left,right)

def merge(left,right):
    res=[]
    while left and  right:
        if left[0]>right[0]:
            res.append(left.pop(0))
        else:
            res.append(right.pop(0))
    res=res+left+right
    return res



A = [3,6,2,3]
print(largestPerimeter(A))
