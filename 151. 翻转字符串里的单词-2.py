class Solution:
    def reverseWords(self, s: str) -> str:
        res=s.split()
        return " ".join(res[::-1])

s = "  hello world!  "
print(Solution().reverseWords(s))



