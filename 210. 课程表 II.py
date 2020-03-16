class Solution:
    def findOrder(self, numCourses: int, prerequisites):
        from collections import deque
        if numCourses == 0: return []
        des = [[] for _ in range(numCourses)]
        ingreed = [0 for _ in range(numCourses)]
        for first, second in prerequisites:
            des[second].append(first)
            ingreed[first] += 1
        stack = deque()
        for i in range(len(ingreed)):
            if ingreed[i] == 0:
                stack.append(i)
        res = []
        while stack:
            cur = stack.popleft()
            res.append(cur)
            numCourses-=1
            for j in des[cur]:
                ingreed[j]-=1
                if ingreed[j]==0:
                    stack.append(j)
        return res if numCourses==0 else []
