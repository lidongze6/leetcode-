class Solution:
    def compressString(self, S: str) -> str:
        S += '-' # S结尾添加了一个-以避免尾部特殊判断
        cnt, n, encoded = 1, len(S), ""

        for i in range(1, n):
            if S[i] == S[i - 1]:
                cnt += 1
            else:
                encoded += S[i - 1] + str(cnt)
                cnt = 1

        return S[:-1] if len(encoded) >= n - 1 else encoded

S="aabcccccaaa"
print(Solution().compressString(S))