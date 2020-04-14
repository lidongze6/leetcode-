class Solution:
    def numsSameConsecDiff(self, N: int, K: int):
        if N == 1: return [i for i in range(10)]

        tmp = set([i for i in range(1,10)])
        for i in range(1, N):
            ans = set()
            while tmp:
                cur = tmp.pop()
                mod = cur % 10
                if mod + K < 10:
                    ans.add(cur * 10 + (mod + K))
                if mod - K >= 0:
                    ans.add(cur * 10 + (mod - K))
            tmp = ans
        return list(ans)
