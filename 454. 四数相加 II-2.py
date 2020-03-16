def fourSumCount(A, B, C, D):
    dict1 = dict()
    res = 0
    for a in A:
        for b in B:
            targer = a + b
            dict1[targer] = dict1.get(targer, 0) + 1
    for c in C:
        for d in D:
            remain = -(c + d)
            if remain in dict1:
                res += dict1[remain]

    return res
