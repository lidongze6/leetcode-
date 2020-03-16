def findErrorNums(nums):
    from collections import Counter
    s = set(range(1, len(nums) + 1))
    lose = s - set(nums)
    dum = Counter(nums).most_common(1)
    return [dum.pop()[0],lose.pop()]


nums = [1,2,2,4]
print(findErrorNums(nums))
