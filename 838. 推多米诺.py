class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        symbols = [(i, x) for i, x in enumerate(dominoes) if x != '.']
        symbols1 = [(-1, "L")] + symbols
        symbols2 = symbols + [(len(dominoes), "R")]
        res = list(dominoes)
        for l, r in zip(symbols1, symbols2):
            if l[1] == r[1]:
                for k in range(l[0] + 1, r[0]):
                    res[k] = l[1]
            elif l[1] == "R" and r[1] == "L":
                for k in range((r[0] - l[0]-1) // 2):
                    res[l[0]+1 + k] = l[1]
                    res[r[0]-1 - k] = r[1]
        return "".join(res)


dominoes = ".L.R...LR..L.."
print(Solution().pushDominoes(dominoes))
