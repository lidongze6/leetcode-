def findLongestWord(s, d):
    d.sort(key=lambda x:[-len(x),x[0]])
    for str_ in d:
        if ismatched(s,str_):
            max_str=str_
            return max_str
    return ""

def ismatched(s,str_):
    j=0
    for i in s:
        if i==str_[j]:
            j+=1
            if j==len(str_):
                return True
    return False

s="abpcplea"
d=["ale","apple","monkey","plea","alh"]
print(ismatched(s,"apple"))
print(findLongestWord(s,d))