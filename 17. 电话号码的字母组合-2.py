class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        dict1 = {"2": ["a", "b", "c"], "3": ["d", "e", "f"], "4": ["g", "h", "i"], "5": ["j", "k", "l"],
                 "6": ["m", "n", "o"], "7": ["p", "q", "r", "s"], "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"]}
        res = []

        def helper(string, res, index):
            if len(string) == len(digits):
                res.append(string)
                return
            for s in dict1[digits[index]]:
                helper(string + s, res, index + 1)
            return

        helper("", res, 0)
        return res
