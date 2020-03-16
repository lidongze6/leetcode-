import math


def mapri_num(num):
    thre = int(math.sqrt(num))
    i = 2
    while i <= thre:
        if num % i == 0:
            return False
        i += 1
    return True


def prime_number(n):
    """
    给一个n，找出小于等于n的所有素数
    """
    nums = [i + 2 for i in range(n - 1)]
    for j in nums:
        if j and mapri_num(j):
            temp = 2
            while temp * j <= n:
                if nums[temp * j - 2]:
                    nums[temp * j - 2] = 0
                temp += 1
    return [k for k in nums if k != 0]


if __name__ == "__main__":
    n = 30
    print(prime_number(n))
