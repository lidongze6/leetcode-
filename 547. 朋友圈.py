def findCircleNum(M):
    row = len(M)
    visit = set()
    count = 0
    for i in range(row):
        if (i, i) not in visit and M[i][i] == 1:
            stack = [(i, i)]
            while stack:
                cur = stack.pop()
                visit.add(cur)
                for n in range(row):
                    if (n, n) not in visit and M[cur[0]][n] == 1:
                        stack.append((n,n))
            count += 1
    return count


M = [[1, 1, 0],
     [1, 1, 0],
     [0, 0, 1]]
print(findCircleNum(M))
