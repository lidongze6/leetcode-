def maxNumberOfBalloons(text: str) -> int:
    str1 = "balloon"
    return min(text.count(i) // str1.count(i) for i in set(str1))