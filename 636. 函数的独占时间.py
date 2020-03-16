def exclusiveTime(n, logs):
    """
    把所有出现end的时间time都加1
    :param n:
    :param logs:
    :return:
    """
    num_stack = []
    op_stack = []
    time_stack = []
    timeres = [0]*n
    for i in logs:
        l = i.split(":")
        num, op, time = l
        num = int(num)
        time = (int(time)+1) if op=="end" else int(time)
        if num_stack and num == num_stack[-1]:  # 下一个也是本函数
            timeres[num_stack[-1]] += time - time_stack[-1]
            time_stack.append(time)
            # 判断是结束调用还是嵌套
            if op == op_stack[-1]:  # 嵌套
                num_stack.append(num)
                op_stack.append(op)
            else:  # 结束调用
                op_stack.pop()
                num_stack.pop()
        else:
            if num_stack:# 下一个不是本函数
                timeres[num_stack[-1]] += time - time_stack[-1]
            time_stack.append(time)
            num_stack.append(num)
            op_stack.append(op)

    return timeres


logs = ["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"]
n = 1
print(exclusiveTime(n, logs))
