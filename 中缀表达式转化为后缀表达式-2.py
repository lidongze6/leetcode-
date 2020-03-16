def calculate(s):
    ex = transform_expression(s)
    stack = []
    op1 = {"*", "/"}
    op2 = {"+", "-"}

    for char in ex:
        if char.isdigit():
            stack.append(char)
        else:
            right = int(stack.pop())
            left = int(stack.pop())
            if char in op2:
                res = left + right if char == "+" else left - right
            elif char in op1:
                res = left * right if char == "*" else left // right
            stack.append(res)

    return res


def transform_expression(s):
    # 中缀表达式---》后缀表达式
    op1 = {"*", "/"}
    op2 = {"+", "-"}
    op = {"*", "/", "+", "-", "(", ")"}
    op_stack = []
    string = []
    nums = 0
    for n, char in enumerate(s):
        if char.isdigit():
            nums = nums * 10 + int(char)
            if n + 1 < len(s) and s[n + 1].isdigit():
                continue
            else:
                string.append(str(nums))
                nums = 0
        elif char in op:
            if char == "(":
                op_stack.append(char)
            elif char == ")":
                while op_stack and op_stack[-1] != "(":
                    string.append(op_stack.pop())
                op_stack.pop()
            else:
                if not op_stack:
                    op_stack.append(char)
                else:
                    while op_stack and (op_stack[-1] in op1 or (op_stack[-1] in op2 and char in op2)):
                        string.append(op_stack.pop())
                    op_stack.append(char)
    while op_stack:
        string.append(op_stack.pop())

    return string


# 中缀表达式
infix_expression = "12 * (3 + 4) - 6 + 8 / 2"
print(calculate(infix_expression))
