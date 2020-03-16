class Solution:
    def maxProfitAssignment(self, difficulty, profit, worker):
        diff_pro = zip(difficulty, profit)
        diff_pro = sorted(diff_pro, key=lambda x: x[1], reverse=True)
        worker.sort()
        res = 0
        for diff, pro in diff_pro:
            for w in worker[::-1]:
                if w >= diff:
                    worker.pop()
                    res += pro
        return res


difficulty = [2, 4, 6, 8, 10]
profit = [10, 20, 30, 40, 50]
worker = [4, 5, 6, 7]
print(Solution().maxProfitAssignment(difficulty, profit, worker))
