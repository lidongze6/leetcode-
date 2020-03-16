class StockSpanner:
    """
    单调栈
    核心：找到当前price之前的第一个比他大的值的位置，计算两者的差值
    """

    def __init__(self):
        self.stack=[] #二维数组[price,count]

    def next(self, price):
        count=1
        if self.stack and self.stack[-1][0]==price: # 如果刚收到的price的值与他前一个值相等，则直接count+1节省时间
            count=self.stack.pop()[1]+1
        while self.stack and self.stack[-1][0]<=price:
            count=self.stack[-1][1]+count
            self.stack.pop()

        self.stack.append([price,count])

        return self.stack[-1][1]


