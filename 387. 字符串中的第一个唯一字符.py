def firstUniqChar(s: str) -> int:
    letter = "abcdefghijklmnopqrstuvwzyz"
    index = [s.index(l) for l in letter if s.count(l) == 1]
    return min(index) if len(index) > 0 else -1