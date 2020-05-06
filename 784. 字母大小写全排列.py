class Solution:
    def letterCasePermutation(self, S: str):
        res = []
        S=S.lower()
        def helper(res, tmp, index):
            if len(tmp) == len(S):
                res.append(tmp)
            else:
                if S[index].isalpha():
                    for j in [1, -1]:
                        if j == 1:
                            helper(res, tmp + S[index].upper(), index + 1)
                        else:
                            helper(res, tmp + S[index], index + 1)
                else:
                    helper(res, tmp + S[index], index + 1)
            return

        helper(res, "", 0)
        return res
S = "12345"
print(Solution().letterCasePermutation(S))
