def removeDuplicates(s, k):
    stack = []
    for char in s:
        if not stack:
            stack.append([1, char])
        elif stack[-1][1] == char:
            if stack[-1][0] == k - 1:
                n = k - 1
                while n > 0:
                    stack.pop()
                    n -= 1
            else:
                stack.append([stack[-1][0] + 1, char])
        else:
            stack.append([1, char])

    return "".join(i[1] for i in stack)


s = "deeedbbcccbdaa"
k = 3
print(removeDuplicates(s, k))
