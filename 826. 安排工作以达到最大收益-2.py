class Solution:
    def maxProfitAssignment(self, difficulty, profit, worker):
        diff_pro = sorted(zip(difficulty, profit), key=lambda x: x[1], reverse=True)
        worker.sort(reverse=True)
        i = 0
        l = len(diff_pro)
        res = 0
        for w in worker:
            while i < l and w < diff_pro[i][0]:
                i += 1
            if i < l:
                res += diff_pro[i][1]
            else:
                break
        return res


difficulty = [2, 4, 6, 8, 10]
profit = [10, 20, 30, 40, 50]
worker = [4, 5, 6, 7]
print(Solution().maxProfitAssignment(difficulty, profit, worker))
