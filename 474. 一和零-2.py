class Solution:
    def findMaxForm(self, strs, m: int, n: int) -> int:
        # 空间优化,但此时要逆序遍历
        l = len(strs)
        if l < 1: return 0
        f=[[0] * (n + 1) for i in range(m + 1)]

        for k in range(l+1):
            c0=strs[k-1].count("0")
            c1=strs[k-1].count("1")
            for i in range(m,c0-1,-1):
                for j in range(n,c1-1,-1):
                    if i>=c0 and j>=c1:
                        f[i][j]=max(f[i][j],f[i-c0][j-c1]+1)
        return f[m][n]


Array = ["10", "0001", "111001", "1", "0"]
m = 5
n = 3
print(Solution().findMaxForm(Array, m, n))

