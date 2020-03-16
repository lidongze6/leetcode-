def getPermutation(n, k):
    res = []
    nums = [i for i in range(1, n + 1)]
    if n==1:
        return "1"

    def factoraical(n):
        if n == 1 or n==0:
            return 1
        return n * factoraical(n - 1)

    def helper(lst, res, k, nums):
        if len(nums) == 0:
            res.append(lst)
        for i in range(len(nums)):
            helper(lst + str(nums[i]), res, k, nums[:i] + nums[i + 1:])
            if len(res) == k:
                return res[k - 1]

    tmp = factoraical(n - 1)
    startnum = k // tmp
    step = k % tmp
    if step==0:
        return helper(str(nums[startnum-1]), res, tmp, nums[:startnum-1] + nums[startnum:])
    else:
        return helper(str(nums[startnum]), res, step, nums[:startnum] + nums[startnum + 1:])


print(getPermutation(1, 1))
