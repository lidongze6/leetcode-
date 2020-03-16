def relativeSortArray(arr1,arr2):
    if not arr2:
        return sorted(arr1)
    l=len(arr1)
    j=0
    for i in arr2:
        tmp=j
        for m in range(j,l):
            if arr1[m]==i:
               arr1[m],arr1[tmp]=arr1[tmp],arr1[m]
               tmp+=1
        j=tmp
    arr1[j:]=sorted(arr1[j:])
    return arr1


