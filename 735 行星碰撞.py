def asteroidCollision(asteroids):
    stack=[]
    eq=1
    for i in asteroids:
        if not stack or (stack and stack[-1]*i)>=0:
            stack.append(i)
        while stack and stack[-1]*i<0:
            if abs(stack[-1])>abs(i):
                break
            elif abs(stack[-1])==abs(i):
                stack.pop()
                eq=0
                break
            elif abs(stack[-1])<abs(i):
                stack.pop()
        if not stack and eq:
            stack.append(i)
    return stack




asteroids = [-2,1,-2,1]
print(asteroidCollision(asteroids))



