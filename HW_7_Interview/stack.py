class Stack:

    def __init__(self, list_input):
        self.list_input = list_input

    def is_empty(self):
        return self.list_input == []

    def push(self, elem):
        self.list_input.append(elem)

    def pop(self):
        return self.list_input.pop()

    def peek(self):
        return self.list_input[-1]

    def size(self):
        return len(self.list_input)
    def pr(self):
        print(self.list_input)