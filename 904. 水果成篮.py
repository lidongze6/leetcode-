class Solution:
    def totalFruit(self, tree) -> int:
        s = dict()
        l, r = 0, 0
        res = 0
        for r in range(len(tree)):
            if len(s) < 2 or len(s) == 2 and tree[r] in s:
                s[tree[r]] = s.get(tree[r], 0) + 1
                res = max(res, r - l)
            elif len(s) == 2 and tree[r] not in s:
                while l <= r and len(s) == 2:
                    s[tree[l]] -= 1
                    if s[tree[l]] == 0:
                        del s[tree[l]]
                    l += 1
                s[tree[r]] = s.get(tree[r], 0) + 1
        return res
