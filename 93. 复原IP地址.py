"""
给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。
输入: "25525511135"
输出: ["255.255.11.135", "255.255.111.35"]
"""
def restoreIpAddresses(s):
    l=len(s)
    res=[]
    helper(res,[],0,s)
    return res

def helper(res,str1,startindex,s):
    if len(str1)==4:
        res.append(str1[:])
        return

    for i in range(startindex,4):
        for j in range(1,4):
            str1.append(j)
            helper(res,str1,j,s)
            str1.pop()

print(restoreIpAddresses("25525511135"))
