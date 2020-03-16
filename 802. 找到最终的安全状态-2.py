class Solution:
    def eventualSafeNodes(self, graph):
        # dfs
        l=len(graph)
        if l==1:return [0]
        flag=[0]*l
        res=[]
        connect=dict()
        for i in range(l):
            connect[i]=graph[i]
        for i in range(l):
            if self.dfs(i,flag,connect):
                res.append(i)
        return res

    def dfs(self,cur,flag,connect):
        if flag[cur]==1:
            # 说明有环 返回False
            return False
        if flag[cur]==-1:
            # 说明在其他节点访问过了，无环，返回True
            return True
        flag[cur]=1
        for i in connect[cur]:
            if not self.dfs(i,flag,connect):
                return False

        flag[cur]=-1
        return True


graph = [[1, 2], [2, 3], [5], [0], [5], [], []]
s = Solution()
print(s.eventualSafeNodes(graph))
