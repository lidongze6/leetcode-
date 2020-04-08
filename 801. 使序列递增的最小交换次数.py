class Solution:
    def minSwap(self, A, B) -> int:
        l = len(A)
        if l <= 1: return 0
        swap, not_swap = 1, 0
        for i in range(1, l):
            if A[i] > A[i - 1] and B[i] > B[i - 1]:
                if A[i] > B[i - 1] and B[i] > A[i - 1]:
                    not_swap,swap =min(swap, not_swap),min(swap, not_swap) + 1
                else:
                    swap=swap+1
                    not_swap=not_swap
            else:
                not_swap,swap=swap,not_swap+1
        return min(swap,not_swap)


A=[1,3,5,4]
B=[1,2,3,7]
print(Solution().minSwap(A,B))