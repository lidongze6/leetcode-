def max_sequece(ones):
    """
    给一个只包含1,0的数组，找出最长的全是1的子数组
    """
    left=right=0
    maxium=left-right
    while right<len(ones):
        if ones[right]==0:
            maxium=max(maxium,right-left)
            left=right+1
        right+=1
    return maxium


def max_sequece_1(ones):
    local=maxium=0
    for i in ones:
        local=local+1 if i==1 else 0
        maxium=max(maxium,local)
    return maxium




ones=[0,1,0,0,1,1,1,1,0,1]
print(max_sequece(ones))
print(max_sequece_1(ones))
