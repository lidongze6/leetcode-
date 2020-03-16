def findCircleNum(M):
    count = 0
    row = len(M)
    for i in range(row):
        if M[i][i] == 1:
            stack = [i]
            while stack:
                cur = stack.pop()
                M[cur][cur] = 0
                for j in range(row):
                    if M[cur][j] == 1 and M[j][j] == 1:
                        stack.append(j)
            count += 1
    return count


M = [[1, 1, 0],
     [1, 1, 0],
     [0, 0, 1]]
print(findCircleNum(M))
