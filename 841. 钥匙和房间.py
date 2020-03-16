class Solution:
    def canVisitAllRooms(self, rooms):
        l = len(rooms)
        if l == 0: return False
        if l == 1: return True
        connect = dict()
        for i in range(l):
            connect[i] = rooms[i]
        stack = [0]
        visit = set()
        while stack:
            key = stack.pop()
            visit.add(key)
            for i in connect[key]:
                if i not in visit:
                    stack.append(i)

        return len(visit) == l


rooms = [[1,3],[3,0,1],[2],[0]]
s = Solution()
print(s.canVisitAllRooms(rooms))
