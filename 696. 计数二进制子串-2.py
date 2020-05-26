class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        # 分组的看有多少个连续的值
        helper = s.replace('01', '0 1').replace('10', '1 0').split()
        h = list(map(len, helper))
        return sum(min(a, b) for a, b in zip(h, h[1:]))



s="00110011"
