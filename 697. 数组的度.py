def findShortestSubArray(nums):
    l = len(nums)
    dict1 = {}
    for i in range(l):
        if nums[i] not in set(dict1.keys()):
            dict1[nums[i]] = [1, i, i]
        else:
            dict1[nums[i]][2] = i
            dict1[nums[i]][0] += 1

    count = -1
    dist = l
    for j in dict1.items():
        dis = j[1][2] - j[1][1] + 1
        if j[1][0] > count or (j[1][0] == count and dis < dist):
            count = j[1][0]
            dist = dis

    return dist


if __name__ == "__main__":
    nums = [1, 2, 2, 3, 1, 4, 2]
    print(findShortestSubArray(nums))
