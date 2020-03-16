def sortArrayByParityII(A):
    if not A:return A
    l=len(A)
    for i in range(l):
        tmp=i
        while tmp<l:
            if (i%2==0 and A[tmp]%2!=0)or(i%2 !=0 and A[tmp]%2==0):
                tmp+=1
            else:break
        A[tmp],A[i]=A[i],A[tmp]
    return A






A=[4,2,5,7]
print(sortArrayByParityII(A))
