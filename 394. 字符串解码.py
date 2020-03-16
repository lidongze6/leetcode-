def decodeString(s):
    numstack = []
    strstack = []
    num = 0
    this_str = ''

    for i in s:
        if i.isdigit():
            num = num * 10 + int(i)  # 防止出现超过10的数字
        elif i.isalpha():
            this_str = this_str + i  # 防止出现连续字母
        elif i == "[":
            numstack.append(num)
            strstack.append(this_str)
            num = 0
            this_str = ""
        else:
            this_str = strstack.pop() + numstack.pop() * this_str

    return this_str



s="3[a]2[bc]"
print(decodeString(s))
