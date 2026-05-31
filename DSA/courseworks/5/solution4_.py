class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val, self.min_stack[-1]))

    def pop(self):
        if self.stack:
            self.stack.pop()
            self.min_stack.pop()

    def top(self):
        return self.stack[-1] if self.stack else None

    def getMin(self):
        return self.min_stack[-1] if self.min_stack else None


ops = ["MinStack","push","push","push","getMin","pop","top","getMin"]
vals = [[],[-2],[0],[-3],[],[],[],[]]

obj = MinStack()

for op, val in zip(ops, vals):
    if op == "push":
        obj.push(val[0])
        print("null")
    elif op == "pop":
        obj.pop()
        print("null")
    elif op == "top":
        print(obj.top())
    elif op == "getMin":
        print(obj.getMin())
    else:
        print("null")