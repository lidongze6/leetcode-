"""
给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。
"""
def generateParenthesis(n):
    res=[]
    str1=""

    generateParenthesis_help(str1,res,n,n)
    return res

def generateParenthesis_help(str1, res, left_num, right_num):
    # Base
    if right_num == 0:
        res.append(str1)
    if left_num>0:
        generateParenthesis_help(str1+"(", res, left_num-1, right_num)
    if right_num>left_num:
        generateParenthesis_help(str1+")", res, left_num, right_num-1)

print(generateParenthesis(3))