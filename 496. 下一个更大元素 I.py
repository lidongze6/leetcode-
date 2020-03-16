def nextGreaterElement(nums1, nums2):
    stack = []
    dic = {}
    for i in range(len(nums2) - 1, -1, -1):
        while stack and nums2[i] >= stack[-1]:
            stack.pop()
        if not stack:
            dic[nums2[i]]=-1
        elif stack and nums2[i]<stack[-1]:
            dic[nums2[i]]=stack[-1]
        stack.append(nums2[i])

    return [dic.get(i,-1) for i in nums1]



num1=[1,3,5,2,4]
num2=[6,5,4,3,2,1,7]
print(nextGreaterElement(num1,num2))

