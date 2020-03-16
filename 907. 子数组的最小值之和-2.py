def sumSubarrayMins(A):
    ans = 0
    A = [float('-inf')] + A + [float('-inf')]
    stack = []
    for i, a in enumerate(A):
        while stack and A[stack[-1]] > a:
            cur = stack.pop()
            ans += A[cur] * (i - cur) * (cur - stack[-1])
        stack.append(i)
    return ans % (10 ** 9 + 7)




A = [3,1,2,4]
print(sumSubarrayMins(A))
