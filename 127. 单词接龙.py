class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:
        from collections import deque
        if not wordList: return 0
        alph = "abcdefghijklmnopqrstuvwxyz"
        not_visit = set(wordList)
        stack=deque()
        stack.append((beginWord, 1))
        while stack:
            word, lengh = stack.popleft()
            if word == endWord:
                return lengh
            for i in range(len(word)):
                for j in alph:
                    new_word = word[:i] + j + word[i + 1:]
                    if new_word in not_visit:
                        not_visit.remove(new_word)
                        stack.append((new_word, lengh + 1))
        return 0


beginWord = "qa"
endWord = "sq"
wordList = ["si", "go", "se", "cm", "so", "ph", "mt", "db", "mb", "sb", "kr", "ln", "tm", "le", "av", "sm", "ar", "ci",
            "ca", "br", "ti", "ba", "to", "ra", "fa", "yo", "ow", "sn", "ya", "cr", "po", "fe", "ho", "ma", "re", "or",
            "rn", "au", "ur", "rh", "sr", "tc", "lt", "lo", "as", "fr", "nb", "yb", "if", "pb", "ge", "th", "pm", "rb",
            "sh", "co", "ga", "li", "ha", "hz", "no", "bi", "di", "hi", "qa", "pi", "os", "uh", "wm", "an", "me", "mo",
            "na", "la", "st", "er", "sc", "ne", "mn", "mi", "am", "ex", "pt", "io", "be", "fm", "ta", "tb", "ni", "mr",
            "pa", "he", "lr", "sq", "ye"]
s = Solution()
print(s.ladderLength(beginWord, endWord, wordList))
