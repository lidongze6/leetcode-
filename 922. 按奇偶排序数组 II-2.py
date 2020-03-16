def sortArrayByParityII(A):
    if not A:return A
    l=len(A)

    j=1
    for i in range(0,l,2):
        if A[i]%2==1:
            while A[j]%2 !=0:
                j+=2
            A[i],A[j]=A[j],A[i]
    return A


A=[4,2,5,7]
print(sortArrayByParityII(A))