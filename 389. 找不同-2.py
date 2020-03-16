def findTheDifference(s: str, t: str) -> str:
    """
    collections.Counter 提供了加减方法。
    Counter(t) - Counter(s)后返回值就是多出来的字母，list()后返回即可。

    """
    from collections import Counter
    return list(Counter(t) - Counter(s))[0]

