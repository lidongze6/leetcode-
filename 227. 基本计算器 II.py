def calculate(s):
    op1 = {"*", "/"}
    op2 = {"+", "-"}
    numstack = []
    opstack = []
    tmp = 0
    for n, char in enumerate(s):
        if char.isdigit():
            tmp = tmp * 10 + int(char)
            if n + 1 < len(s) and s[n + 1].isdigit():
                continue
            else:
                numstack.append(tmp)
                tmp=0
        elif char in op1:  # char 为*或/
            if opstack:
                while opstack:
                    if opstack[-1] in op1:
                        sym = opstack.pop()
                        num2 = numstack.pop()
                        num1 = numstack.pop()
                        res = num1 * num2 if sym == "*" else num1 // num2
                        numstack.append(res)
                    elif opstack[-1] in op2:
                        break
                opstack.append(char)
            else:
                opstack.append(char)
        elif char in op2:  # char 为+ 或 -
            if opstack:
                while opstack:
                    if opstack[-1] in op2:  # char 为+ 或 -
                        sym = opstack.pop()
                        num2 = numstack.pop()
                        num1 = numstack.pop()
                        res = num1 + num2 if sym == "+" else num1 - num2
                        numstack.append(res)
                    elif opstack[-1] in op1:  # char 为* 或/
                        sym = opstack.pop()
                        num2 = numstack.pop()
                        num1 = numstack.pop()
                        res = num1 * num2 if sym == "*" else num1 // num2
                        numstack.append(res)
                opstack.append(char)
            else:
                opstack.append(char)
    ans = 0
    while opstack:
        op = opstack.pop()
        nu2 = numstack.pop()
        nu1 = numstack.pop()
        if op in op1:
            ans = nu1 * nu2 if op == "*" else nu1 // nu2
        elif op in op2:
            ans = nu1 + nu2 if op == "+" else nu1 - nu2
        numstack.append(ans)

    return numstack.pop()


s = "3+2*2"
print(calculate(s))
