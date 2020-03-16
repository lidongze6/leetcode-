def shortestCompletingWord(licensePlate, words):
    from collections import Counter
    licensePlate = licensePlate.lower()
    li = Counter(dict([[l, licensePlate.count(l)] for l in licensePlate if l.isalpha()]))
    words.sort(key=lambda x: len(x))
    for word in words:
        if len(li - Counter(word)) == 0:
            return word


licensePlate = "B687015"
words=["born","give","would","nice","in","understand","blue","force","have","that"]
print(shortestCompletingWord(licensePlate, words))
