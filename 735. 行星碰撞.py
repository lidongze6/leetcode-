def asteroidCollision(asteroids):
    if len(asteroids) <= 1:
        return asteroids
    l, r = 0, len(asteroids) - 1
    mid = l + (r - l) // 2
    left = asteroidCollision(asteroids[l:mid + 1])
    right = asteroidCollision(asteroids[mid + 1:r + 1])

    while left and right:
        if left[-1] * right[0] >= 0:  # 说明同号，不会撞到一起
            return left + right
        elif left[-1] < 0 and right[0] > 0:  # left 往左移动，right往右移动，不会撞到一起
            return left + right
        else:
            if abs(left[-1]) > abs(right[0]):
                right.pop(0)
            elif abs(left[-1]) < abs(right[0]):
                left.pop()
            else:
                left.pop()
                right.pop(0)
    return left + right


asteroids = [10, 2, -5]
print(asteroidCollision(asteroids))
