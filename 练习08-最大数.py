"""
给定一个数组，数组里有一个数组有且只有一个最大数，判断这个最大数是否是其他数的两倍或更大。如果存在这个数，则返回其index，否则返回-1。
"""
def largest_twice(nums):
    second_max=first_max=float("-inf")
    index=0
    for n,i in enumerate(nums):
        if i>first_max:
            second_max,first_max=first_max,i
            index=n
        elif i>second_max: # i比first_max小，比second_max大
            second_max=i

    return index if first_max>2*second_max else -1



nums=[1,2,3,8,5,2,1]
print(largest_twice(nums))