def relativeSortArray(arr1, arr2):
    if not arr2:
        return sorted(arr1)
    c=[0 for _ in arr2]
    res=[0 for _ in arr1]
    unappear=[]
    for i in arr1:
        if i in arr2:
            c[arr2.index(i)]+=1
        else:
            unappear.append(i)
    for j in range(1,len(c)):
        c[j]+=c[j-1]
    for n in arr1:
        if n in arr2:
            res[c[arr2.index(n)]-1]=n
            c[arr2.index(n)]-=1
    res[len(arr1)-len(unappear):]=sorted(unappear)
    return res


arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]
print(relativeSortArray(arr1,arr2))
