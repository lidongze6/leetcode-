
def calPoints(ops):
    """
    :type ops: List[str]
    :rtype: int
    """
    list1 = []
    for i in ops:
        if i.isdigit() or (i.strip('-')).isdigit():
            list1.append(int(i))
        else:
            if len(list1) == 0:
                continue
            if i == "+":
                list1.append(list1[-1] + list1[-2])
            if i == "D":
                list1.append(list1[-1] * 2)
            if i == "C":
                list1.pop()

    sum = 0
    for j in list1:
        sum = sum + j
    return sum



ops=["-21","-66","39","+","+"]
print(calPoints(ops))