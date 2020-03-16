def repeatedNTimes(A):
    from collections import Counter
    return Counter(A).most_common(1)[0]
