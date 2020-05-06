class Solution:
    def toHex(self, num: int) -> str:
        li = "0123456789abcdef"
        if num == 0: return "0"
        # 将负数转化为正数，即补码转换为正码,因为题目已告知为32位有符号整数，0xFFFFFFFF二进制为4,294,967,296
        num &= 0xFFFFFFFF
        res = ""
        while num > 0:
            res = li[num & 15] + res
            num = num >> 4

        return res


print(Solution().toHex(-1))
