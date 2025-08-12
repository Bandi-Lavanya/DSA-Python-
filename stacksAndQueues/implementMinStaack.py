'''
["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"]
[[],        [-2],   [0],    [-3],    [],       [],    [],    []]
'''
'''
Create MinStack → []

push(-2) → Stack = [(-2, -2)] (value, current min)

push(0) → Stack = [(-2, -2), (0, -2)]

push(-3) → Stack = [(-2, -2), (0, -2), (-3, -3)]

getMin() → -3

pop() → Remove (-3, -3) → Stack = [(-2, -2), (0, -2)]

top() → 0

getMin() → -2'''
class Pair:
    def __init__(self, x, y):
        self.x = x  # value
        self.y = y  # current min


class MinStack:
    def __init__(self):
        self.st = []  # stack to store Pair objects

    def push(self, x):
        if not self.st:
            current_min = x
        else:
            current_min = min(self.st[-1].y, x)
        self.st.append(Pair(x, current_min))

    def pop(self):
        if self.st:
            self.st.pop()

    def top(self):
        if self.st:
            return self.st[-1].x
        return None  # or raise exception

    def getMin(self):
        if self.st:
            return self.st[-1].y
        return None  # or raise exception


# Example usage
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
print(obj.getMin())  # -3
obj.pop()
print(obj.top())     # 0
print(obj.getMin())  # -2


class MinStack:
    def __init__(self):
        self.st = []
        self.mini = float('inf')

    def push(self, value):
        val = value
        if not self.st:
            self.mini = val
            self.st.append(val)
        else:
            if val < self.mini:
                # Store encoded value
                self.st.append(2 * val - self.mini)
                self.mini = val
            else:
                self.st.append(val)

    def pop(self):
        if not self.st:
            return
        val = self.st.pop()
        if val < self.mini:
            # Retrieve previous min
            self.mini = 2 * self.mini - val

    def top(self):
        if not self.st:
            return None
        val = self.st[-1]
        if val < self.mini:
            return self.mini
        return val

    def getMin(self):
        return self.mini
ms = MinStack()
ms.push(5)
ms.push(3)
ms.push(7)
print(ms.getMin())  # 3
ms.pop()
print(ms.top())     # 3
print(ms.getMin())  # 3
ms.pop()
print(ms.getMin())  # 5
