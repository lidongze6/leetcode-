class Solution:
    def balancedStringSplit(self, s: str) -> int:
        if not s: return 0
        return self.dfs(s,0)[0]

    def dfs(self, s, idx):
        if idx == len(s):
            return 0, idx
        l, r = 0, 0
        res = 0
        while idx < len(s):
            if s[idx] == "L":
                l += 1
            else:
                r += 1
            if l == r:
                num, idx = self.dfs(s, idx + 1)
                res += 1+num
            idx += 1
        return res, idx


s = "RLRRLLRLRL"
print(Solution().balancedStringSplit(s))
