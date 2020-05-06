class Solution:
    def toHex(self, num: int) -> str:
        if num == 0: return "0"
        num &= 0xFFFFFFFF
        res = ""
        dic = {10: "a", 11: "b", 12: "c", 13: "d", 14: "e", 15: "f"}

        while num:
            num, mod = divmod(num, 16)
            if mod >= 10:
                res += dic[mod]
            else:
                res += str(mod)

        return res[::-1]


print(Solution().toHex(-1))
