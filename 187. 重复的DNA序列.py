def findRepeatedDnaSequences(s):
    from collections import defaultdict
    if len(s) <= 10:
        return []

    l = 0
    r = 9
    dict1 = defaultdict(int)
    while r < len(s):
        dict1[s[l:r + 1]] += 1
        r += 1
        l += 1
    return filter(lambda i:dict1[i]>1,dict1)

s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
print(findRepeatedDnaSequences(s))