def uncommonFromSentences(A, B):
    li1 = A.split(" ")
    li2 = B.split(" ")
    list1 = [char for char in li1 if li1.count(char) == 1 and li2.count(char) == 0]
    list2 = [char for char in li2 if li2.count(char) == 1 and li1.count(char) == 0]

    return list1 + list2


A = "apple apple"
B = "banana"
print(uncommonFromSentences(A, B))
