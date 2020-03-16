class Solution:
    def threeSumMulti(self, A, target: int) -> int:
        A.sort()
        count = 0
        for i, num in enumerate(A):
            l, r = i + 1, len(A) - 1
            remain = target - num
            while l < r:
                if A[l] + A[r] > remain:
                    r -= 1
                elif A[l] + A[r] < remain:
                    l += 1
                elif A[l] + A[r] == remain and A[l] != A[r]:
                    ll, rr = l, r
                    while l < r and A[l] == A[l + 1]:
                        l += 1
                    while l < r and A[r] == A[r - 1]:
                        r -= 1
                    count += (rr - r + 1) * (l - ll + 1)
                    l += 1
                    r -= 1
                elif A[l] + A[r] == remain and A[l] == A[r]:
                    ll, rr = l, r
                    count += (rr - ll + 1) * (rr - ll) // 2
                    break
        return count


A = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
target = 8
print(Solution().threeSumMulti(A, target))
