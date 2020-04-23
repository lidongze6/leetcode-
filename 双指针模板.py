def two_pointers(nums):
    l,r=0,0
    while r<len(nums)-1:
        while 条件不满足 and r<len(nums)-1:
            r += 1
            改变条件
        while 满足条件 and l<=r:
            更改满足条件的结果数
            改变条件
            l+=1