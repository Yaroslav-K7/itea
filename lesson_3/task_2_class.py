class Stack:

    def __init__(self):
        self.new_list = []

    def push(self, x):
        self.new_list.append(x)

    def my_list(self):
        return self.new_list

    def del_(self):
        try:
            return self.new_list.pop()

        except IndexError as e:
            return e

class Queue(Stack):
    def __init__(self):
        super().__init__()

    def push(self, x):
        self.new_list.insert(0, x)
