class Solution:
    def compressString(self, S: str) -> str:
        if not S: return ""
        res=""
        l,r=0,0
        length=len(S)
        for r in range(length):
            if 0<r<length and S[r]==S[r-1]:
                continue
            if r>0 and S[r] !=S[r-1]:
                res=res+S[l]+str(r-l)
                l=r
        res=res+S[l]+str(length-l)
        return res if len(res)<length else S