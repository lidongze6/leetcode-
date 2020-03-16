def hIndex(citations):
    """
    找到h个大于等于h，N-h个小于等于h的数的最大值h
    """
    if not citations:
        return 0
    citations.sort()
    max_index = 0
    for i in range(len(citations)-1,-1,-1):
        if citations[i]>=max_index+1:
            max_index += 1
        else:
            break

    return max_index


citations = [100]
print(hIndex(citations))
