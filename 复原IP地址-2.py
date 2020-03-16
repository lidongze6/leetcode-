def restoreIpAddresses(s):
    l = len(s)
    res = []
    helper(res, [], 0, s, l)
    for i in range(len(res)):
        res[i] = ".".join(res[i])
    return res


def helper(res, str1, startindex, s, length_remain):
    if length_remain == 0 and int(str1[-1]) <= 255:
        res.append(str1[:])
        return

    for j in range(1,4):
        if length_remain>=j:
            if int(s[:j])>255 or (j >= 3 and int(s[:j]) < 100) or (j >= 2 and int(s[:j]) < 10):
                continue
            if len(str1)==4 and length_remain>0:
                break
            str1.append(s[:j])
            helper(res,str1,startindex+1,s[j:],length_remain-j)
            str1.pop()

print(restoreIpAddresses("25525511135"))