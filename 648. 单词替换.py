def replaceWords(dic, sentence):
    dict1 = dict()
    list1 = sentence.split(" ")
    for i, char in enumerate(list1):
        if char in dict1:
            list1[i] = dict1[char]
        else:
            for j in range(len(dic))[::-1]:
                if char[:len(dic[j])] == dic[j] and len(char) > len(dic[j]):
                    dict1[char] = dic[j]
                    list1[i] = dic[j]
    return " ".join(list1)


dic = ["a", "aa", "aaa", "aaaa"]
sentence = "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa"
print(replaceWords(dic, sentence))
