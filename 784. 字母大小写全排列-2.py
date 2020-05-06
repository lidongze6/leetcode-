class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        res=[]
        def helper(res,tmp,S):
            if not S:
                res.append(tmp)
            else:
                if S[0].isalpha():
                    helper(res,tmp+S[0].upper(),S[1:])
                    helper(res,tmp+S[0].lower(),S[1:])
                else:
                    helper(res,tmp+S[0],S[1:])
            return
        helper(res,"",S)
        return res