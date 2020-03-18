class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # 回溯，超时
        if len(t) < len(s): return False
        res = set()

        def helper(index, res, tmp):
            res.add(tmp)
            for i in range(index, len(t)):
                helper(i + 1, res, tmp + t[i])

        helper(0, res, "")
        if s in res:
            return True
        else:
            return False


s = "abc"
t = "ahbgdc"
print(Solution().isSubsequence(s, t))
