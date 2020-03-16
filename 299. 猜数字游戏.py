def getHint(secret: str, guess: str) -> str:
    dict1 = {}
    set1 = set(secret)
    set2 = set()
    A_count = 0
    for i in range(len(secret)):
        dict1[i] = secret[i]

    for j in range(len(guess)):
        if guess[j] in set1 and dict1[j] !=guess[j]:
            set2.add(guess[j])
        elif guess[j] in set1 and dict1[j] ==guess[j]:
            A_count += 1
    return str(A_count) + "A" + str(len(set2)) + "B"


secret = "1122"
guess = "2211"
print(getHint(secret, guess))
