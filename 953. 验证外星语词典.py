def isAlienSorted(words, order):
    dic = {}
    for i, char in enumerate(order):
        dic[char] = i
    for i in range(1, len(words)):
        x = False
        for j in range(min(len(words[i]), len(words[i - 1]))):
            if dic[words[i - 1][j]] < dic[words[i][j]]:
                x = True
                break
            elif dic[words[i - 1][j]] > dic[words[i][j]]:
                return False
        if not x and len(words[i - 1]) > len(words[i]):
            return False
    return True

words = ["hello", "leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"
print([1,2,3]>[1,1,1])
