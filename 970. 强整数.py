def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
    import math
    a_list = []
    x_num = math.floor(math.log(bound, x)) if x != 1 else 1
    y_num = math.floor(math.log(bound, y)) if y != 1 else 1
    for item in range(x_num + 1):
        for i in range(y_num + 1):
            num = x ** item + y ** i
            if num <= bound:
                a_list.append(num)
    return list(set(a_list))