class Solution:
    def canReach(self, arr, start: int) -> bool:
        # DFS
        l = len(arr)
        if l == 1 and arr[0] == 0: return True
        dic = dict()
        s = set()

        def dfs(cur):
            if arr[cur] == 0: return True
            if cur in s: return False
            if cur in dic:
                return dic[cur]
            else:
                s.add(cur)
                dic[cur] = (0 <= cur - arr[cur] < l and dfs(cur - arr[cur])) or (
                        0 <= cur + arr[cur] < l and dfs(cur + arr[cur]))
                return dic[cur]

        return dfs(start)


arr = [3, 0, 2, 1, 2]
start = 2
print(Solution().canReach(arr, start))
