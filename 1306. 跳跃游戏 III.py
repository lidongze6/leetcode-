class Solution:
    def canReach(self, arr, start: int) -> bool:
        # BFS
        l = len(arr)
        if l == 1 and arr[0] == 0: return True
        dic = set()
        dic.add(start)
        stack = [start]
        while stack:
            cur = stack.pop(0)
            if arr[cur] == 0: return True
            for i in [-1, 1]:
                if 0 <= cur + i * arr[cur] < l and cur + i * arr[cur] not in dic:
                    stack.append(cur + i * arr[cur])
                    dic.add(cur + i * arr[cur])
        return False
