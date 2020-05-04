class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        start = 1
        while start <= n:
            if start == n:
                return True
            start = start << 1
        return False


print(Solution().isPowerOfTwo(16))
