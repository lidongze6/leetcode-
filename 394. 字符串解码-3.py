def decodeString(s):
    stack = [["",1]]
    nums = ""
    for char in s:
        if char.isdigit():
            nums += char
        elif char == "[":
            stack.append(["", nums])
            nums = ""
        elif char == "]":
            st, k = stack.pop()
            stack[-1][0] += st * int(k)
        elif char.isalpha():
            stack[-1][0] += char

    return stack[0][0]


s = "3[a]2[b4[F]c]"
print(decodeString(s))
