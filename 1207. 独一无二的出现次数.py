def uniqueOccurrences(arr):
    from collections import Counter
    c = Counter(arr)
    return len(set(c.values())) == len(c)


arr = [-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]
print(uniqueOccurrences(arr))
