class Solution:
    def countBits(self, num: int) -> List[int]:
        # 位运算DP
        # f[i]=f[i>>1](右移一位)+i最后一位是0还是1
        if num==0:return [0]
        f=[0]*(num+1)
        f[1]=1
        for i in range(2,num+1):
            f[i]=(i&1)+f[i>>1]
        return f