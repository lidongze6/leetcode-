class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        from collections import Counter
        import math
        l = len(deck)
        if l <= 1: return False
        c = Counter(deck)
        mingcd = min(c.values())
        for i in c.values():
            if i == 1: return False
            mingcd = math.gcd(mingcd, i)
            if mingcd == 1:
                return False
        return True
