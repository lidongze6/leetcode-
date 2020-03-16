def singleNumber(nums):
    set1 = set()
    for num in nums:
        if num in set1:
            set1.remove(num)
        else:
            set1.add(num)

    return set1.pop()


nums=[2,2,1]
print(singleNumber(nums))