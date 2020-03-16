def asteroidCollision(asteroids):
    res = []
    for num in asteroids:
        while len(res) > 0:
            if res[-1] < 0 or num * res[-1] >= 0:
                res.append(num)
                break
            elif abs(num) == abs(res[-1]):
                res.pop()
                break
            elif abs(num) > abs(res[-1]):
                res.pop()
            elif abs(num) < abs(res[-1]):
                break
        else:
            res.append(num)
    return res


asteroids = [-2, 1, -2, 1]
print(asteroidCollision(asteroids))
