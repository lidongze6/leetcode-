
def countPrimes(n):
    # 厄拉多塞筛法
    if n < 3:
        return 0
    # 首先生成一个全部为1的列表
    output = [1] * n
    output[0], output[1] = 0, 0
    for i in range(2, int(n ** 0.5) + 1):
        if output[i] == 1:  # 如果i为质数
            output[i * i:n:i] = [0] * len(output[i * i:n:i])  # 将i的倍数置为0
    return sum(output)