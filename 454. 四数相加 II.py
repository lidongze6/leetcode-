def fourSumCount(A, B, C, D):
    from collections import Counter
    dict1=Counter(a + b for a in A for b in B)
    return sum(dict1.get(-c - d, 0) for c in C for d in D)


A = [0, 1, -1]
B = [-1, 1, 0]
C = [0, 0, 1]
D = [-1, 1, 1]
print(fourSumCount(A, B, C, D))
