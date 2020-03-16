class Solution:
    def intervalIntersection(self, A, B):
        # 别人的，可见自己写的有多烂
        i, j = 0, 0
        res = []
        while i < len(A) and j < len(B):
            a_left, a_right = A[i][0], A[i][1]
            b_left, b_right = B[j][0], B[j][1]
            if b_right >= a_left and a_right >= b_left:
                res.append([max(a_left, b_left), min(a_right, b_right)])
            if b_right < a_right:
                j += 1
            else:
                i += 1

        return res
