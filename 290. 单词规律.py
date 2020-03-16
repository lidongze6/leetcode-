def wordPattern(pattern, str1):
    res=str1.split()
    return list(map(pattern.index, pattern))==list(map(res.index,res))



pattern = "abba"
str1 = "dog dog dog dog"
print(wordPattern(pattern,str1))