def distributeCandies(candies):
    s = set(candies)
    if len(s) <= len(candies) // 2:
        return len(s)
    else:
        c = len(s) - (len(candies) - len(s))
        return len(s) - (c // 2)


candies = [1, 1, 2, 3]
print(distributeCandies(candies))
