class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        n1, n2 = len(A), len(B)
        t = int(n2 / n1) + 1
        ls = [t - 1, t, t + 1]
        for i in ls:
            if B in A * i:
                return i
        return -1
