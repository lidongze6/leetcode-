def minAddToMakeValid(S):
    S=S.replace("()","")
    return len(S)

S="()))(("
print(minAddToMakeValid(S))