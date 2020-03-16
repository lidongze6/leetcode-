def decodeAtIndex(S, K):
    """
    结果一定在S中，因此我们没有必要把S展开再求。
    而且这样做(当测试样例"y959q969u3hb22odq595")会出现内存溢出的现象。
    因此可以想办法在原始S中求第K位，
        1.算出展开S的长度为size，
        2.所求位置为K%size。因此倒序遍历S，
            遇见数字size=size/d，因为K对size的倍数求余和对size求余是一样的
            遇见字母N=N-1; 因为K%size不为说明当前不是要找的字母，
        直到K%size==0。输出此处字符
    :param S:
    :param K:
    :return:
    """
    size = 0
    # Find size = length of decoded string
    for c in S:
        if c.isdigit():
            size *= int(c)
        else:
            size += 1

    for c in reversed(S):
        K %= size
        if K == 0 and c.isalpha():
            return c

        if c.isdigit():
            size /= int(c)
        else:
            size -= 1



S = "leet2code3"
k=10
print(decodeAtIndex(S,k))
