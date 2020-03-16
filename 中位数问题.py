import heapq
"""
给定一个数组，返回它的每个数字前的所有数字的中位数
例[2,3,5,1,7,9]---->[2,3,3,3,3,5]
"""

def midnumber(nums):
    less_heaq = []  # 小根堆，存放n/2个较大值
    more_heaq = []  # 大根堆，存放n/2个较小值
    res=[]

    for i in nums:
        if not less_heaq and not more_heaq:
            heapq.heappush(more_heaq, -1 * i)
        else:
            if i > -1*heapq.nsmallest(1, more_heaq)[0]:
                heapq.heappush(less_heaq, i)
            else:
                heapq.heappush(more_heaq, -1 * i)

            if len(more_heaq) - len(less_heaq) > 1:
                tmp = -1 * heapq.heappop(more_heaq)
                heapq.heappush(less_heaq, tmp)
            elif len(less_heaq) - len(more_heaq) > 1:
                tmp = -1 * heapq.heappop(less_heaq)
                heapq.heappush(more_heaq, tmp)

        if len(more_heaq)>len(less_heaq):
            res.append(-1*heapq.nsmallest(1,more_heaq)[0])
        else:
            res.append(heapq.nsmallest(1,less_heaq)[0])
    return res


if __name__ == "__main__":
    nums = [4, 2, 5, 7, 9, 1, 3, 5, 2, 5, 8, 10]
    print(midnumber(nums))

