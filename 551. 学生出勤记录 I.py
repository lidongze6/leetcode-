class Solution:
    def checkRecord(self, s: str) -> bool:
        Acount = 0
        for i in range(len(s)):
            if i > 1 and s[i] == "L" and s[i - 1] == "L" and s[i - 2] == "L":
                return False
            if s[i] == "A":
                Acount += 1
                if Acount > 1:
                    return False
        return True
