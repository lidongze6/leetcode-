def strStr(haystack, needle):
    l = len(needle)
    h = len(haystack)
    if l == 0:
        return 0

    if l == h:
        if needle == haystack:
            return 0
        else:
            return -1
    else:
        for i in range(h - l+1):
            if haystack[i:i + l] == needle:
                return i
        return -1


if __name__ == "__main__":
    haystack = "mississippi"
    needle = "pi"
    print(strStr(haystack, needle))
