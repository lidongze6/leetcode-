def beautifulArray(N):
    # 奇偶拆分
    if N == 2:
        return [1, 2]
    elif N == 1:
        return [1]
    left = beautifulArray((N+1) // 2)
    right = beautifulArray(N // 2)
    left_list = [i * 2 - 1 for i in left]
    right_list = [j * 2 for j in right]

    return left_list + right_list


print(beautifulArray(4))
