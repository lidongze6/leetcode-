def calculate(s):
    """当遇到符号时候，将前一次的符号连同前一次的数字进行计算保存到res，并更新sym为新的符号
        当遇到数字时候，用tmp记录临时数字
        当遇到（时候，将res和当前的符号入栈
        当遇到）时候，先计算括号前面最后一个数字的结果，在将stack出栈，计算stack与res的结果
        最后再有数字再单独计算一次
    """
    res = 0  # 记录结果
    sym = "+"  # 记录前一次的符号
    tmp = 0  # 记录当前的数字
    stack = []

    for char in s:
        if char.isdigit():
            tmp = tmp * 10 + int(char)
        elif char == "(":
            stack.append([res, sym])
            res = 0
            sym = "+"
        elif char == ")":
            res = res + tmp if sym == "+" else res - tmp
            tmp = 0
            tp, k = stack.pop()
            if k == "+":
                res = tp + res
            else:
                res = tp - res
        elif char == " ":
            continue
        else:
            res = res + tmp if sym == "+" else res - tmp
            tmp = 0
            sym = char
    ans = res + tmp if sym == "+" else res - tmp
    return ans


s = "(1+(2-13)+4)-(5-6)+17"
print(calculate(s))
