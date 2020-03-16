def lengthOfLastWord(s):
    list1 = []
    n = 0
    # 记录‘ ’ 个数，且若下一个不为‘ ’，则n=0
    for i in s:
        if i != ' ':
            if n == 0:
                list1.append(i)
            else:
                list1.clear()
                list1.append(i)
                n = 0
        elif i == ' ':
            n += 1
            list1.append(i)
    return len(list1) - n



print(lengthOfLastWord("Hello World"))