"""
Given two integers a ≤ b, write a program  that transforms a into b by a minimum sequence of increment (add 1) and unfolding (multiply by 2) operations.

For example,

23 = ((5 * 2 + 1) * 2 + 1)

113 = ((((11 + 1) + 1) + 1) * 2 * 2 * 2 + 1)
"""


def intSeq(a, b):
    # 递归版本
    if a == b:
        return str(a)
    if b >= 2 * a:
        if b % 2 == 1:
            return "(" + intSeq(a, b - 1) + "+1)"
        else:
            return "(" + intSeq(a, b // 2) + "*2)"
    else:
        return "(" + intSeq(a, b - 1) + "+1)"


def inSeq1(a, b):
    # 循环版本
    res = ""
    count = 0
    while a < b:
        if b >= 2 * a:
            if b % 2 == 1:
                res = "+1)" + res
                b -= 1
            else:
                res = "*2)" + res
                b = b // 2
        else:
            res = "+1)" + res
            b -= 1
        count += 1
    if a == b:
        res = "(" * count + str(a) + res
    return res


print(intSeq(5, 23))
print(inSeq1(5, 23))
