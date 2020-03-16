class Solution(object):
    def snakesAndLadders(self, board):
        from collections import deque
        N = len(board)
        nums = [-1]
        for i in range(N):
            if i % 2 == 0:
                nums += board[N - 1 - i]
            else:
                for j in range(N - 1, -1, -1):
                    nums.append(board[N - 1 - i][j])
        min_step = [400] * (N * N + 1)
        min_step[1] = 0
        stack = deque()
        stack.append([1, 0])
        while stack:
            cur, step = stack.popleft()
            if cur == N * N:
                return step
            for i in range(6, 0, -1):
                if cur + i <= N * N:
                    if nums[cur + i] != -1 and step + 1 < min_step[nums[cur + i]]:
                        min_step[nums[cur + i]] = step + 1
                        stack.append([nums[cur + i], step + 1])
                    elif nums[cur + i] == -1 and step + 1 < min_step[cur + i]:
                        min_step[cur + i] = step + 1
                        stack.append([cur + i, step + 1])
        return -1


board = [[-1, -1, -1, -1, -1, -1],
         [-1, -1, -1, -1, -1, -1],
         [-1, -1, -1, -1, -1, -1],
         [-1, 35, -1, -1, 13, -1],
         [-1, -1, -1, -1, -1, -1],
         [-1, 15, -1, -1, -1, -1]]

s = Solution()
print(s.snakesAndLadders(board))
