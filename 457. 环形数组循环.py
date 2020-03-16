class Solution:
    def circularArrayLoop(self, nums):
        if len(nums) == 1: return False
        l = len(nums)
        test = [False] * l
        for i in range(l):
            if not test[i]:
                visit = set()
                while True:
                    next_i = i + nums[i]
                    if next_i >= 0:
                        next_i = next_i % l
                    else:
                        while next_i<0:
                            next_i = l + next_i
                    test[next_i] = True
                    if next_i == i: break
                    if nums[next_i] * nums[i] < 0 or (next_i in visit and len(visit) == 1 and visit.pop() == next_i):
                        break
                    if next_i in visit and len(visit) >= 2:
                        return True
                    visit.add(next_i)
                    i = next_i
        return False


nums = [-2,-3,-9]
print(Solution().circularArrayLoop(nums))
