class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        lst = list(s)

        for i in range(0, len(lst), 2 * k):
            lst[i: i + k] = lst[i: i + k][::-1]

        return ''.join(lst)


s = "sakdjdhqweg"
k = 3
print(Solution().reverseStr(s, k))
