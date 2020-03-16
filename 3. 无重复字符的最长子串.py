def lengthOfLongestSubstring(s):
    # 递归，超时
    if len(set(s)) == len(s):
        return len(s)
    i = 0
    tmp = dict()
    l = 0
    while i < len(s) and s[i] not in tmp:
        tmp[s[i]] = i
        i += 1
        l += 1
    start = tmp[s[i]]
    return max(l, lengthOfLongestSubstring(s[start + 1:]))


s="pwwkew"
print(lengthOfLongestSubstring(s))

