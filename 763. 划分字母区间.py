class Solution:
    def partitionLabels(self, S):
        if len(S) == 0: return []
        if len(S) == 1: return [1]
        dic = dict()
        l, r = 0, 0
        dic[S[l]] = l
        for r in range(len(S)):
            if S[r] in dic:
                for i in dic.keys():
                    if dic[S[r]] < dic[i] < r:
                        dic[i] = dic[S[r]]
            else:
                dic[S[r]] = r
        res = sorted(set(dic.values()))
        res.append(len(S))
        return [res[i] - res[i - 1] for i in range(1, len(res))]


S = "ababcbacadefegdehijhklij"
print(Solution().partitionLabels(S))
