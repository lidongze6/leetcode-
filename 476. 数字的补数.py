class Solution:
    def findComplement(self, num: int) -> int:
        b = str(bin(num))
        b = b[2:]
        out = 0
        by = 1
        for c in b[::-1]:
            if c == "0":
                out += by
            by *= 2  # 1,2,4,8准则

        return out

print(Solution().findComplement(5))