class Solution:
    def minJumps(self, arr) -> int:
        # BFS 关键点是对connections中的连续相同的值只需记录首位位置，其余删除即可，否则会超时
        from collections import deque
        from collections import defaultdict
        l = len(arr)
        visit = set()
        stack = deque()
        stack.append(0)
        connetions = defaultdict(list)
        for i in range(len(arr)):
            # 如果当前index和dict中已记录的值的最后一个是连续的，则把dict中的尾部值删除，并加入当前的值
            if len(connetions[arr[i]]) > 1 and connetions[arr[i]][-1] + 1 == i:
                connetions[arr[i]].pop()
            connetions[arr[i]].append(i)

        step = 0
        while stack:
            for i in range(len(stack)):
                cur = stack.popleft()
                if cur == l - 1:
                    return step
                for i in [-1, 1]:
                    if 0 <= cur + i < l and cur + i not in visit:
                        visit.add(cur + i)
                        stack.append(cur + i)
                for j in connetions[arr[cur]]:
                    if j not in visit:
                        visit.add(j)
                        stack.append(j)
            step += 1
