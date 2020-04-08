class Solution:
    def rotate(self, matrix):
        l=len(matrix)
        for i in range(l//2):
            for j in range(i,l-i-1):
                tmp=matrix[j][i]
                matrix[j][i]=matrix[l-1-i][j]
                matrix[l-1-i][j]=matrix[l-1-j][l-1-i]
                matrix[l-1-j][l-1-i]=matrix[i][l-1-j]
                matrix[i][l-1-j]=tmp


matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
Solution().rotate(matrix)
print(matrix)