class Solution:
    def sortedSquares(self, A):
        return sorted([i**2 for i in A])


A = [-3,-3,-2,1]
print(Solution().sortedSquares(A))
