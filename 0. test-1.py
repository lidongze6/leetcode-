def letterCombinations(digits):
    res = []
    helper(res, [], digits, 0)
    return res


def helper(res, list, digits, po):
    if len(list) == len(digits):
        res.append(list[:])
        return

    for i in range(po, len(digits)):
        for j in range(len(digits[i])):
            list.append(digits[i][j])
            helper(res, list, digits, i + 1)
            list.pop()


print(letterCombinations([["a","b","c"], ["x", "y", "z"]]))