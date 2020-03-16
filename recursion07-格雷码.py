def greycode(n):
    import copy
    # for 循环版本
    if n == 1:
        print("enter", 1)
    res = [["enter", 1]]
    for i in range(2, n + 1):
        tmp = copy.deepcopy(res)  # 两层list，必须导入copy模块实现深拷贝否则都是浅拷贝
        tmp[len(tmp) // 2][0] = "exit"
        res = res + [["enter", i]] + tmp
    for j, m in res:
        print(j, m)


def greycode1(n, po):
    # bad 递归版本 递归深度造成内存不足
    if n == 1:
        print("enter", 1) if po == True else print("exit", 1)
    greycode1(n - 1, True)
    print("enter", n) if po == True else print("exit", n)
    greycode1(n - 1, False)


greycode(3)
greycode1(3, True)
