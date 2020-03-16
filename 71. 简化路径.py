def simplifyPath(path):
    path = path.split("/")
    stack = []

    for i in path:
        if i != "":
            if i == ".." and stack:
                stack.pop()
            elif i != ".." and i != ".":
                stack.append(i)

    return "/" + "/".join(stack)


path = "/home/"
print(simplifyPath(path))

set1 = set("+-*/")
print(int(-1/3))
