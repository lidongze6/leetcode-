class Solution:
    def removeStones(self, stones):
        import itertools
        import collections
        # 并查集
        count = len(stones)
        stones = list(map(tuple, stones))
        parent = collections.defaultdict(list)
        for i in stones:
            parent[i] = i

        def find(cur):
            while parent[cur] != cur:
                parent[cur] = parent[parent[cur]]
                cur = parent[cur]
            return cur

        def union(i, j):
            nonlocal count
            p1 = find(i)
            p2 = find(j)
            if p1 == p2:
                return
            parent[p2] = p1
            count -= 1

        for c1, c2 in itertools.combinations(stones, 2):
            if c1[0] == c2[0] or c1[1] == c2[1]:
                union(c1, c2)
        return len(stones)-count


stones = [[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]
s = Solution()
print(s.removeStones(stones))
