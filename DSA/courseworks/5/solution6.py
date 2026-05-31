class MyQueue:

    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x):
        self.in_stack.append(x)

    def _transfer(self):
        while self.in_stack:
            self.out_stack.append(self.in_stack.pop())

    def pop(self):
        if not self.out_stack:
            self._transfer()
        return self.out_stack.pop()

    def peek(self):
        if not self.out_stack:
            self._transfer()
        return self.out_stack[-1]

    def empty(self):
        return not self.in_stack and not self.out_stack


ops = ["MyQueue", "push", "push", "peek", "pop", "empty"]
vals = [[], [1], [2], [], [], []]

obj = MyQueue()

for op, val in zip(ops, vals):
    if op == "push":
        obj.push(val[0])
        print("null")
    elif op == "pop":
        print(obj.pop())
    elif op == "peek":
        print(obj.peek())
    elif op == "empty":
        print(obj.empty())
    else:
        print("null")