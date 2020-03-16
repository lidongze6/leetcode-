def quicksort(alist, beg, end):
    # alist 表示数组
    # beg为开始位置
    # end 为结束位置

    # 递归结束条件,即只有一个元素时，默认为有序数组
    if beg >= end:
        return

    # 定义中间元素 mid_value为起始位置值
    mid_value = alist[beg]
    # 定义左侧右侧指针 left right
    left = beg
    right = end

    while left < right:
        # 若右侧指针对应元素大于mide_value，则继续将指针向左移动直到遇到小于mide_value的位置
        while left < right and alist[right] >= mid_value:
            right -= 1
        # 若左侧指针对应元素小于mide_value，则继续将指针向右移动直到遇到大于mide_value的位置
        while left < right and alist[left] <= mid_value:
            left += 1

        alist[left], alist[right] = alist[right], alist[left]

    # 循环结束时，此时right，left指针位置重叠,交换起始位置元素与当前指针位置元素

    alist[beg], alist[right] = alist[right], alist[beg]

    quicksort(alist, beg, right-1)
    quicksort(alist, right + 1, end)


if __name__ == "__main__":
    n = input("输入")
    n=int(n)
    q = list()
    for i in range(n):
        q.append(int(input()))

    quicksort(q, 0, n - 1)
    print(q)
