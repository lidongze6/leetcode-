def countAndSay(n):
    # 应该是迭代
    if n == 1:
        return "1"

    while n > 1:
        str1 = countAndSay(n - 1)
        if str1 == "1":
            return "11"
        str2 = ""
        count = 1
        beg = 0
        for i in range(1, len(str1)):
            if str1[i] == str1[beg]:
                count += 1
            else:
                str2 = str2 + str(count) + str1[beg]
                count = 1
            beg += 1
        str2 = str2 + str(count) + str1[beg]
        return str2


if __name__ == "__main__":
    print(countAndSay(4))
