class Solution:
    def videoStitching(self, clips, T: int):
        clips.sort()
        n=clips[-1][1]
        f = [[101] * (n + 1) for i in range(n + 1)]
        for i in range(n + 1):
            f[i][i] = 0

        for k in range(1, n + 1):
            for i in range(n + 1 - k):
                j = i + k  # f[i][j]
                for c in clips:
                    if c[0] > j or c[1] < i:
                        continue
                    elif c[0] <= i and j <= c[1]:
                        f[i][j] = min(f[i][j], 1)
                    elif i <= c[0] and c[0] <= j:
                        if c[1] >= j:
                            f[i][j] = min(f[i][j], f[i][c[0]] + 1 + f[j][c[1]])
                        else:
                            f[i][j] = min(f[i][j], f[i][c[0]] + 1 + f[c[1]][j])
        return f[0][T] if f[0][T] < 101 else -1


clips = [[0, 4], [2, 8]]
T = 5
print(Solution().videoStitching(clips, T))
