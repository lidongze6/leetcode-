class Solution:
    def reverseWords(self, s: str) -> str:
        s.lstrip()
        s.rstrip()
        res = []
        tmp = ""
        for n, c in enumerate(s):
            if c != " ":
                tmp += c
            else:
                if tmp != "":
                    res.append(tmp)
                    tmp = ""
        if tmp !="":
            res.append(tmp)
        return " ".join(res[::-1])


s = "  hello world!  "
print(Solution().reverseWords(s))
