def hIndex(citations) -> int:
    """
    找到h个大于等于h的数的最大的h
    :param citations:
    :return:
    """
    if not citations or citations[-1]==0:return 0
    l,r=0,len(citations)-1
    while l<r:
        mid=(l+r)//2
        if len(citations)-mid>citations[mid]:
            l=mid+1
        else:r=mid

    if l>=r:
        return len(citations)-l


citations = [0]
print(hIndex(citations))