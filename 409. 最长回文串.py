def longestPalindrome(s: str) -> int:
    li = list(set(s))
    flag = False
    res = 0
    for l in li:
        res += s.count(l) // 2
        if s.count(l)%2 !=0:
            flag=True
    return res * 2 + 1 if flag else res*2


s = "bb"
print(longestPalindrome(s))
