class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 回溯+贪心，超时
        coins.sort(reverse=True)
        res=-1
        def helper(remain,step):
            nonlocal res
            if remain==0:
                res=min(res,step) if res !=-1 else step
                return
            for cur in coins:
                if res !=-1:
                    break
                if remain-cur<0:
                    continue
                helper(remain-cur,step+1)
            return
        helper(amount,0)
        return res
