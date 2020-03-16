def merge(intervals):
    intervals.sort(key=lambda x:x[0])
    res=[]
    for i in intervals:
        if not res or res[-1][1]<i[0]:
            res.append(i)
        elif res[-1][1]>=i[0]:
            tmp=res.pop()
            res.append([tmp[0],max(tmp[1],i[1])])
    return res


intervals=[[1,6],[12,26],[11,18],[5,8]]
print(merge(intervals))