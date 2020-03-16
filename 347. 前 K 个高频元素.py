def topKFrequent(nums, k):
    from collections import Counter
    c = Counter(nums)
    return c.most_common(k)


