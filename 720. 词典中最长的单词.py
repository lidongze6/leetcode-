def longestWord(words):
    words.sort(key=lambda x: (-len(x), x))
    s = set(words)
    for char in words:
        flag = False
        for i in range(1, len(char) + 1):
            if char[:i] not in s:
                flag = False
                break
            else:
                flag = True
        if flag:
            return char
    return ""


words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
print(longestWord(words))
