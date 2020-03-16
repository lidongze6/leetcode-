"""
程序接受三个参数m，n，p，然后生成m*n的矩阵，然后每一个cell有p的概率是地雷
生成矩阵后，在计算出每一个cell周围地雷的数量
"""

import random


def minesweeper(m, n, p):
    board = [[None for i in range(n + 2)] for j in range(m + 2)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            r = random.random()
            board[i][j] = -1 if r < p else 0

    for i in range(1,m+1):
        for j in range(1,n+1):
            print("*",end=" ") if board[i][j]==-1 else print(".",end=" ")
        print("\n")

    for i in range(1,m+1):
        for j in range(1,n+1):
            if board[i][j]==".":
                for ii in range(i-1,i+1):
                    for jj in range(j-1,j+1):
                        if board[ii][jj]=="*":
                            board[i][j]+=1

    print("\n")
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            print("*", end=" ") if board[i][j] == -1 else print(board[i][j], end=" ")
        print("\n")

minesweeper(5, 10, 0.4)
