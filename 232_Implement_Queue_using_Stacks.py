class MyQueue:

    def __init__(self):
        self.in_stack = []
        self.out_stack = []
        self.len_in = 0

    def push(self, x: int) -> None:
        self.in_stack.append(x)
        self.len_in += 1

    def pop(self) -> int:
        print("pop")
        if self.out_stack == []:
            self.move()
        out = self.out_stack.pop()
        print("pop: ", self.out_stack)
        return out

    def peek(self) -> int:
        print("peek")
        if self.out_stack == []:
            self.move()
        out = self.out_stack[-1]
        print("peek: ", self.out_stack)
        return out

    def empty(self) -> bool:
        return self.in_stack == [] and self.out_stack == []

    def move(self) -> None:
        print("before")
        print("in_: ", self.in_stack)
        print("out: ", self.out_stack)
        for i in range(self.len_in):
            out = self.in_stack.pop()
            self.out_stack.append(out)
        print("after")
        print("in_: ", self.in_stack)
        print("out: ", self.out_stack)
        self.len_in = 0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()