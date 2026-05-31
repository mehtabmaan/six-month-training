from collections import deque

class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x):
        self.q.append(x)
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self):
        return self.q.popleft()

    def top(self):
        return self.q[0]

    def empty(self):
        return len(self.q) == 0


ops = ["MyStack", "push", "push", "top", "pop", "empty"]
vals = [[], [1], [2], [], [], []]

obj = MyStack()

for op, val in zip(ops, vals):
    if op == "push":
        obj.push(val[0])
        print("null")
    elif op == "pop":
        print(obj.pop())
    elif op == "top":
        print(obj.top())
    elif op == "empty":
        print(obj.empty())
    else:
        print("null")