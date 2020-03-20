def letterCombinations(digits,k):
    import heapq
    heapq.heapify(digits)
    res=heapq.nsmallest(k,digits)
    return res

digits=[0,1,2,1]
k=2
print(letterCombinations(digits,k))