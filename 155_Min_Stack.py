class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, value: int) -> None:
        # print('push')
        # print('stack__: ', self.stack)
        # print('stack_m: ', self.min_stack)
        self.stack.append(value)
        if self.min_stack == []:
            self.min_stack.append(value)
        elif self.min_stack[-1] >= value:
            self.min_stack.append(value)

    def pop(self) -> None:
        # print('pop')
        # print('stack__: ', self.stack)
        # print('stack_m: ', self.min_stack)
        pop_value = self.stack.pop()
        if self.min_stack[-1] == pop_value:
            self.min_stack.pop()
        # print('stack__: ', self.stack)
        # print('stack_m: ', self.min_stack)

    def top(self) -> int:
        # print('top')
        # print('stack__: ', self.stack)
        # print('stack_m: ', self.min_stack)
        return self.stack[-1]

    def getMin(self) -> int:
        # print('getMin')
        # print('stack__: ', self.stack)
        # print('stack_m: ', self.min_stack)
        return self.min_stack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()