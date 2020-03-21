class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        from collections import deque
        if x +y <z:return False
        stack=deque()
        visit=set()
        stack.append((x,y))
        while stack:
            a,b=stack.popleft()
            if a==z or b==z or a+b==z:return True
            next_stack=set()
            next_stack.add((a,y))
            next_stack.add((x,b))
            next_stack.add((a,0))
            next_stack.add((0,b))
            if a>y-b:
                next_stack.add((a-y+b,y))
            else:
                next_stack.add((0,a+b))
            if b>x-a:
                next_stack.add((x,b-x+a))
            else:
                next_stack.add((a+b,0))
            for item in next_stack:
                if item not in visit:
                    visit.add(item)
                    stack.append(item)
        return False
