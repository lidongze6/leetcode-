class Solution:
    def numRescueBoats(self, people, limit: int) -> int:
        # 类似于two sum
        people.sort()
        l, r = 0, len(people) - 1
        res, tmp = 0, limit - people[0]
        while l < r:
            if people[r] > tmp:
                r -= 1
                res += 1
            else:
                r -= 1
                l += 1
                res += 1
                tmp = limit - people[l]

        if l == r:
            res += 1
        return res