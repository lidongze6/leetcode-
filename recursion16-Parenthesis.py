def generateParenthesis(n):
    res = []
    backTracking('', n, n, res)
    return res


def backTracking(str1, left_num, right_num, res):
    if right_num == 0:
        res.append(str1)
    if left_num > 0:
        backTracking(str1 + '(', left_num - 1, right_num, res)
    if right_num > left_num:
        backTracking(str1 + ')', left_num, right_num - 1, res)
