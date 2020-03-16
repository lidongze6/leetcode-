class Solution:
    def canFinish(self, numCourses, prerequisites):
        des = [[] for _ in range(numCourses)]
        for i in range(len(prerequisites)):
            des[prerequisites[i][1]].append(prerequisites[i][0])
        for cur in range(numCourses):
            stack = [cur]
            visit=set()
            while stack:
                index= stack.pop()
                visit.add(index)
                for i in des[index]:
                    if i in visit:return False
                    else:
                        stack.append(i)
        return True


numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
s = Solution()
print(s.canFinish(numCourses, prerequisites))
