def removeDuplicates(s, k):
    # 递归
    count = 0
    for n, char in enumerate(s):
        if n == 0:
            count = 1
        else:
            if s[n - 1] == char:
                count += 1
                if count == k:
                    return removeDuplicates(s[:n - k + 1] + s[n + 1:], k)
            else:
                count = 1

    return s


s = "deeedbbcccbdaa"
k = 3
print(removeDuplicates(s, k))
