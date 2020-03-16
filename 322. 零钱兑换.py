def coinChange(coins, amount):
    if amount == 0:
        return 0
    res = []
    for c in coins:
        if amount - c >= 0:
            tmp = coinChange(coins, amount - c)
            if tmp >= 0:
                res.append(1 + tmp)
    return min(res) if res else -1


coins = [5]
amount = 11
print(coinChange(coins, amount))
