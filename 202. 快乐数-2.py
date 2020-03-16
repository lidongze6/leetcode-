def isHappy(n):
    if n == 1:
        return True
    dict1 = {"1": 1, "2": 4, "3": 9, "4": 16, "5": 25, "6": 36, "7": 49, "8": 64, "9": 81, "0": 0}
    set1 = set()
    while True:
        res = sum([dict1[char] for char in str(n)])
        if res == 1:
            return True
        elif res in set1:
            return False
        else:
            set1.add(res)
            n = res


n = 2
print(isHappy(n))
