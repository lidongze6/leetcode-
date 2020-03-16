def isHappy(n):
    set1 = set()
    while True:
        s = 0
        str1 = str(n)
        for i in str1:
            s += int(i) ** 2
        if s == 1:
            return True
        elif s in set1:
            return False
        else:
            set1.add(s)
            n = s



if __name__=="__main__":
    n=19
    print(isHappy(n))