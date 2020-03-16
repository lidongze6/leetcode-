class Solution:
    def isLongPressedName(self, name, typed):
        left = 0
        for j in range(len(typed)):
            if name[left] == typed[j]:
                left += 1
            if left == len(name):
                return True
        return False
