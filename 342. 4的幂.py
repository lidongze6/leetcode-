class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        start = 1
        while start <= num:
            if start == num:
                return True
            start = start << 2
        return False
