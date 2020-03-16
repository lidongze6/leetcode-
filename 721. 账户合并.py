class Solution:
    def accountsMerge(self, accounts):
        from collections import defaultdict
        dict1 = defaultdict(list)
        for num, account in enumerate(accounts):
            for e in range(1, len(account)):
                dict1[account[e]].append(num)
        visit = set()
        res = []
        for i in range(len(accounts)):
            if i not in visit:
                tmp = set()
                self.dfs(i, dict1, visit, tmp, accounts)
                res.append([accounts[i][0]] + sorted(tmp))
        return res

    def dfs(self, num, dict1, visit, tmp, accounts):

        visit.add(num)
        for i in range(1, len(accounts[num])):
            tmp.add(accounts[num][i])
            for j in dict1[accounts[num][i]]:
                if j not in visit:
                    self.dfs(j, dict1, visit, tmp, accounts)
        return


accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"],
            ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]

s = Solution()
print(s.accountsMerge(accounts))
