def hanoi(n, left, mid, right):
    """
    :param n:砝码的数量
    :param left: 左边杆子
    :param mid: 中间杆子
    :param right: 右边杆子
    """
    assert (n>=3)
    if n == 3:
        print(left, "-->", right)
        print(left, "-->", mid)
        print(right, "-->", mid)
        print(left, "-->", right)
        print(mid, "-->", left)
        print(mid, "-->", right)
        print(left, "-->", right)
        return None
    hanoi(n - 1, left, right, mid)
    print(left, "-->", right)
    hanoi(n - 1, mid, left, right)


hanoi(5, left="left", mid="mid", right="right")
