class Solution:
    def findItinerary(self, tickets):
        from collections import defaultdict
        des = defaultdict(list)
        connection = defaultdict(int)
        for first, second in tickets:
            des[first].append(second)
            connection[(first, second)] += 1
        for c in des.values():
            c.sort()
        res = []
        tmp = []
        self.dfs(res, "JFK", tmp, len(tickets), des, connection)
        return res[0]

    def dfs(self, res, string, tmp, count, des, connection):
        if res:return
        if count == 0:
            res.append(tmp + [string])
            return
        for cur in des[string]:
            if connection[(string, cur)] > 0:
                connection[(string, cur)] -= 1
                self.dfs(res, cur, tmp + [string], count - 1, des, connection)
                connection[(string, cur)] += 1
        return


tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
s = Solution()
print(s.findItinerary(tickets))
