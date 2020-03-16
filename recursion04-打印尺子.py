"""
1
1 2 1
1 2 1 3 1 2 1
1 2 1 3 1 2 1 4 1 2 1 3 1 2 1
......
"""


def ruler(n):
    # for
    if n == 1:
        return "1"
    res = "1"
    for i in range(2, n + 1):
        res = res + " " + str(i) + " " + res
    return res


def ruler1(n):
    # bad recursion
    if n == 1:
        return "1"
    return ruler1(n - 1) + " " + str(n) + " " + ruler1(n - 1)


def ruler2(n):
    # recursion
    if n == 1:
        return "1"
    tmp = ruler2(n - 1)
    return tmp + " " + str(n) + " " + tmp


print(ruler(4))
print(ruler1(4))
print(ruler2(4))
