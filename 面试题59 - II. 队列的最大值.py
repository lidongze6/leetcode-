class MaxQueue:
    def __init__(self):
        from collections import deque
        self.max_stack = deque()
        self.stack1 = []
        self.stack2 = []

    def max_value(self) -> int:
        return self.max_stack[0] if self.max_stack else -1

    def push_back(self, value: int) -> None:
        self.stack1.append(value)
        while self.max_stack and self.max_stack[-1] < value:
            self.max_stack.pop()
        self.max_stack.append(value)

    def pop_front(self) -> int:
        if not self.stack2:
            if not self.stack1:
                return -1
            else:
                while self.stack1:
                    self.stack2.append(self.stack1.pop())
        if self.stack2[-1] == self.max_stack[0]:
            self.max_stack.popleft()
        return self.stack2.pop()


