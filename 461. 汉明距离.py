class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # bin函数 返回一个整数 int 或者长整数 long int 的二进制表示。
        return bin(x^y).count("1")