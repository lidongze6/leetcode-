def lengthOfLongestSubstring(s):
    hashset = set()
    tmp = 0
    res = 0
    left = 0  # 用来一会移除set中左边的元素的
    for char in s:
        tmp += 1
        while char in hashset:
            hashset.remove(s[left])
            left+=1
            tmp -= 1
        hashset.add(char)
        res = max(res, tmp)
    return res
