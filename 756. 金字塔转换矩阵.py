class Solution:
    def pyramidTransition(self, bottom: str, allowed):
        import itertools
        from collections import defaultdict
        dict1 = defaultdict(list)
        if not allowed: return False
        for char in allowed:
            dict1[(char[0], char[1])].append(char[2])
        visit = set()

        def dfs(bottom):
            if len(bottom) == 1: return True
            if all((bottom[i], bottom[i + 1]) in dict1 for i in range(len(bottom) - 1)):
                condidate = [dict1[(bottom[i], bottom[i + 1])] for i in range(len(bottom) - 1)]
                if len(condidate) == 1: return True
                for bottom1 in itertools.product(*condidate):
                    new_bottom = "".join(bottom1)
                    if all((new_bottom[i], new_bottom[i + 1]) in visit for i in range(len(new_bottom) - 1)):
                        continue
                    else:
                        for i in range(len(new_bottom) - 1):
                            visit.add((new_bottom[i], new_bottom[i + 1]))
                        if dfs(new_bottom):
                            return True
                        else:
                            for i in range(len(new_bottom) - 1):
                                visit.remove((new_bottom[i], new_bottom[i + 1]))
                return False

        return dfs(bottom)


bottom = "BCD"
allowed = ["ACC", "ACB", "ABD", "DAA", "BDC", "BDB", "DBC", "BBD", "BBC", "DBD", "BCC", "CDD", "ABA", "BAB", "DDC",
           "CCD", "DDA", "CCA", "DDD"]
s = Solution()
print(s.pyramidTransition(bottom, allowed))
