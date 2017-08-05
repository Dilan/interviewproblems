class Stack():
    list = []

    def __init__(self, list):
        self.list = list

    def pop(self):
        return self.list.pop()

    def peek(self):
        return self.list[-1]

    def isEmpty(self):
        return self.list == []

    def size(self):
        return len(self.list)

    def push(self, value):
        print 'value:', value
        self.list.append(value)