class Solution:
    def numEnclaves(self, A):
        row = len(A)
        col = len(A[0])
        stack = []
        visit = set()
        for i in range(row):
            if A[i][0] == 1:
                stack.append([i, 0])
                visit.add((i, 0))
            if A[i][col - 1]:
                stack.append([i, col - 1])
                visit.add((i, col - 1))

        for j in range(col):
            if A[0][j] == 1:
                stack.append([0, j])
                visit.add((0, j))
            if A[row - 1][j] == 1:
                stack.append([row - 1, j])
                visit.add((row - 1, j))

        while stack:
            x, y = stack.pop()
            if A[x][y] == 1:
                A[x][y] = 0
            for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                if 0 <= x + dx < row and 0 <= y + dy < col and (x + dx, y + dy) not in visit and A[x + dx][y + dy] == 1:
                    stack.append([x + dx, y + dy])
                    visit.add((x + dx, y + dy))

        count = 0
        for i in range(row):
            for j in range(col):
                if A[i][j] == 1:
                    count += 1
        return count


A = [[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]
s = Solution()
print(s.numEnclaves(A))
