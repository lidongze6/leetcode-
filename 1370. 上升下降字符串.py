class Solution:
    def sortString(self, s: str) -> str:
        import collections
        str_counter = collections.Counter(s)
        result = []
        flag = False
        while str_counter:
            keys = list(str_counter.keys())
            keys.sort(reverse=flag)
            flag = not flag
            result.append(''.join(keys))
            str_counter -= collections.Counter(keys)
        return ''.join(result)

s =  "leetcode"
print(Solution().sortString(s))