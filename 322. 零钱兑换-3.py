class Solution:
    def coinChange(self, coins, amount: int) -> int:
        # 回溯超时，改用dp
        coins.sort(reverse=True)
        dic = dict()

        def helper(remain):
            if remain in dic:
                return dic[remain]
            if remain == 0: return 0
            if remain < 0: return -1
            res = float("inf")
            for cur in coins:
                tmp = helper(remain - cur)
                if tmp == -1:
                    continue
                res = min(res, 1 + tmp)
            dic[remain] = res if res != float("inf") else -1
            return dic[remain]

        return helper(amount)


coins = [186, 419, 83, 408]
amount = 6249
print(Solution().coinChange(coins, amount))
