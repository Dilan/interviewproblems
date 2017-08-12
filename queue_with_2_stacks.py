# Implement a queue with 2 stacks.
# Your queue should have an enqueue and a dequeue function and it should be "first in first out" (FIFO).
# Optimize for the time cost of [m] function calls on your queue. These can be any mix of enqueue and dequeue calls.
# Assume you already have a stack implementation and it gives O(1) time push and pop.

# Last In First Out
class Stack:
    list = []
    def push(self, item):
        self.list = [item] + self.list;
    def pop(self):
        if len(self.list):
            first = self.list[0]
            self.list = self.list[1:]
            return first
        else:
            return None

class Queue:
    stack1 = Stack()
    stack2 = Stack()

    def enqueue(self, item):
        self.stack1.push(item)
    def dequeue(self):
        if len(self.stack2.list) == 0:
            for index in self.stack1.list:
                self.stack2.push(self.stack1.pop())
        return self.stack2.pop()

# result:
x = Queue()
x.enqueue(1)
x.enqueue(2)
x.enqueue(3)
x.enqueue(4)
print x.dequeue() # 1
print x.dequeue() # 2
x.enqueue(5)
x.enqueue(6)
print x.dequeue() # 3
print x.dequeue() # 4
print x.dequeue() # 5
print x.dequeue() # 6
print x.dequeue() # None
x.enqueue(7)
x.enqueue(8)
print x.dequeue() # 7
print x.dequeue() # 8
