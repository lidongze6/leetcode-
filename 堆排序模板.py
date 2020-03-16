def heap_sort(nums):
    # 将nums抽构成大根堆
    nums=build_heap(nums,len(nums))
    for i in range(len(nums)-1,-1,-1):
        nums[i],nums[0]=nums[0],nums[i] # 交换根节点
        push_down(nums,i,0)
    return nums


def push_down(nums, n, i):
    if i >= n:
        return
    left = i * 2 + 1
    right = i * 2 + 2
    maxi = i
    if left < n and nums[left] > nums[maxi]:
        maxi = left
    if right < n and nums[right] > nums[maxi]:
        maxi = right
    if maxi != i:
        nums[maxi], nums[i] = nums[i], nums[maxi]
        push_down(nums, n, maxi)


def push_up(nums, n, i):
    if (i-1)//2<0:
        return
    father=(i-1)//2
    if father>=0 and nums[father] < nums[i]:
        nums[father], nums[i] = nums[i], nums[father]
        push_up(nums,n,father)


def build_heap(nums,n):
    last_node=n-1
    father=(last_node-1)//2
    for i in range(father,-1,-1):
        push_down(nums,n,i)
    return nums


nums = [4, 10, 2, 5, 1, 3]
nums=nums+[11]
print(heap_sort(nums))


