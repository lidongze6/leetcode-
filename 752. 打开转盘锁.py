class Solution:
    def openLock(self, deadends, target):
        from collections import deque
        visit = set()
        deadends = set(deadends)
        stack = deque()
        stack.append(["0000", 0])

        def neighbors(node):
            for i in range(4):
                x = int(node[i])
                for d in (-1, 1):
                    y = (x + d) % 10
                    yield node[:i] + str(y) + node[i + 1:]

        while stack:
            cur, step = stack.popleft()
            if cur == target: return step
            for new_cur in neighbors(cur):
                if new_cur not in deadends and new_cur not in visit:
                    visit.add(new_cur)
                    stack.append([new_cur, step + 1])

        return -1


deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"]
target = "8888"
s = Solution()
print(s.openLock(deadends, target))
