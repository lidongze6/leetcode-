def exclusiveTime(n,logs):
    res = [0] * n
    stack = []
    for s in logs:
        tmp = s.split(':')
        if tmp[1] == 'start':
            stack.append([int(tmp[0]), int(tmp[2])])
        else:
            temp = stack.pop()
            time = int(tmp[2]) - temp[1] + 1
            res[temp[0]] += time
            if stack:
                res[stack[-1][0]] -= time
    return res


logs = ["0:start:0",
 "1:start:2",
 "1:end:5",
 "0:end:6"]
n = 2
print(exclusiveTime(n, logs))