class Solution:
    def shoppingOffers(self, price, special, needs):
        # 主要是加强filter 和 all的用法
        if sum(needs) == 0: return 0
        special = list(filter(lambda x: x[-1] < sum(x[i] * price[i] for i in range(len(price))), special))
        special = list(filter(lambda x: all(x[i] <= needs[i] for i in range(len(price))), special))
        self.res = 10000
        if not special: return sum(needs[i] * price[i] for i in range(len(price)))
        for pac in special:
            self.res = min(self.res, self.dfs(pac[-1], [needs[i] - pac[i] for i in range(len(price))], special, price))
        return self.res if special else 0

    def dfs(self, value, remain, special, price):
        if sum(remain) == 0:
            return value
        tmp = 10000
        special = list(filter(lambda x: all(x[i] <= remain[i] for i in range(len(price))), special))
        if not special:
            return value + sum(remain[i] * price[i] for i in range(len(price)))
        for new_pac in special:
            tmp = min(tmp, self.dfs(value + new_pac[-1], [remain[i] - new_pac[i] for i in range(len(price))],
                                    special, price))
        return tmp


price = [1, 1, 1]
special = [[1, 1, 1, 0], [2, 2, 1, 1]]
needs = [1, 1, 0]

s = Solution()
print(s.shoppingOffers(price, special, needs))
