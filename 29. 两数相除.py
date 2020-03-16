def divide(dividend, divisor):
    if (dividend>0) ^ (divisor>0):
        po = 0
    else:
        po = 1
    dividend, divisor, = abs(dividend), abs(divisor)
    l, res = dividend, 0
    while l >= divisor:
        i = 1
        r = divisor
        while l >= r:
            l -= r
            res += i
            r += r
            i += i
    res = res if po else (-res)
    return min(max(-2**31, res), 2**31-1)


dividend = -7
divisor = 3
print(divide(dividend, divisor))
print()
