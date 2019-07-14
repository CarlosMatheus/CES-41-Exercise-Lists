class Stack:
    """
    Stack class
    """
    def __init__(self):
        self.s = []

    def pop(self):
        return self.s.pop()

    def top(self):
        return self.s[-1]

    def push(self, elm):
        self.s.append(elm)

    def copy(self):
        return self.s.copy()

    def is_empty(self):
        return len(self.s) == 0
