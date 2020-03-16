def topKFrequent(words, k):
    # 堆
    import heapq
    from collections import Counter
    c = Counter(words)
    list1 = [(-counts, item) for item, counts in c.items()]  # 注意这里list中的元素时元组，heap会先根据元组中的第一个元素排序，再根据第二个排序
    heapq.heapify(list1)
    return [heapq.heappop(list1)[1] for i in range(k)]
