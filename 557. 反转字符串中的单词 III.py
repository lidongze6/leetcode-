class Solution:
    def reverseWords(self, s: str) -> str:
        lst = s.split(" ")
        return " ".join([x[::-1] for x in lst])
