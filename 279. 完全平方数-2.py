class Solution:
    def numSquares(self, n: int) -> int:
        # BFS
        from collections import deque
        stack = deque()
        visit = set()
        stack.append((n, 0))
        while stack:
            num, step = stack.popleft()
            if num == 0: return step
            for i in range(1, int(n ** 0.5) + 1):
                if num-i*i not in visit:
                    stack.append((num-i*i, step + 1))
                    visit.add(num-i*i)
        return -1


print(Solution().numSquares(12))
