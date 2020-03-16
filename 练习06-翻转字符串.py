def revers_str0(str):
    return str[::-1]


def revers_str1(str):
    return "".join(reversed(str))
    # reversed 返回的是一个迭代器



def revers_str2(str):
    l=list(str)
    for i in range(len(l) // 2):
        l[i], l[len(str) - 1 - i] = l[len(str) - 1 - i], l[i]
    return "".join(l)




str="abcdefg"
print(revers_str0(str))
print(revers_str1(str))
print(revers_str2(str))