"nums[a1,a2,...an,b1,b2,...bn]----->[a1,b1,a2,b2....an,bn]"
"且不能使用额外空间"
def exchangesort(nums):
    helper(nums,0,len(nums)-1)
    print(nums)

def helper(nums,left,right):
    if (right - left == 1):
        return

        # Finding mid to divide the array
    mid = (left + right) // 2

    # Using temp for swapping first
    # half of second array
    temp = mid + 1

    # Mid is use for swapping second
    # half for first array
    mmid = (left + mid) // 2

    # Swapping the element
    for i in range(mmid + 1, mid + 1):
        nums[i], nums[temp] = nums[temp], nums[i]
        temp += 1

    # Recursively doing for
    # first half and second half
    helper(nums, left, mid)
    helper(nums, mid + 1, right)

exchangesort([1,2,3,4,5,6,7,8,9,10])
