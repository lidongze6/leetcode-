class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return all([65 <= ord(word[i]) <= 96 for i in range(len(word))]) or all([97 <= ord(word[i]) for i in range(1, len(word))])
