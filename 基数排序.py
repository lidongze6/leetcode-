def radix_sort(nums):
    i = 0  # 记录当前正在排拿一位，最低位为1
    max_num = max(nums)  # 最大值
    j = len(str(max_num))  # 记录最大值的位数
    while i < j:
        bucket_list = [[] for _ in range(10)]  # 初始化桶数组
        for x in nums:
            bucket_list[int(x / (10 ** i)) % 10].append(x)  # 找到位置放入桶数组
        print(bucket_list)
        nums.clear()
        for x in bucket_list:  # 放回原序列
            for y in x:
                nums.append(y)
        i += 1

if __name__ == '__main__':
    a = [334,5,67,345,7,345345,99,4,23,78,45,1,3453,23424]
    radix_sort(a)
    print(a)
