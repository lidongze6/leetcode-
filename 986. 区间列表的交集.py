class Solution:
    def intervalIntersection(self, A, B):
        a, b = 0, 0
        res = []
        while a < len(A) and b < len(B):
            # b 在右边的情况
            if B[b][0] >= A[a][0]:
                if B[b][0] <= A[a][1]:
                    if B[b][1] >= A[a][1]:
                        res.append([B[b][0], A[a][1]])
                        a += 1
                    else:
                        res.append([B[b][0], B[b][1]])
                        b += 1
                else:
                    a += 1
            # a在右边的情况
            elif A[a][0] >= B[b][0]:
                if A[a][0] <= B[b][1]:
                    if A[a][1] >= B[b][1]:
                        res.append([A[a][0], B[b][1]])
                        b += 1
                    else:
                        res.append([A[a][0], A[a][1]])
                        a += 1
                else:
                    b += 1
        return res


A = [[8, 15]]
B = [[2, 6], [8, 10], [12, 20]]
print(Solution().intervalIntersection(A, B))
