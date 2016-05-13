from stack import Stack

class HanoiStack(Stack):
    def __init__(self, list):
        self.list = []
        for value in list:
            self.push(value)

    def push(self, value):
        if not self.isEmpty() and value > self.peek():
            raise StandardError('Value ' + str(value) + ' have to be smaller then ' + str(self.peek()))
        self.list.append(value)


def move(n, source, tmp, dest):
    if n == 1:
        return dest.push(source.pop())

    move(n-1, source, dest, tmp)
    move(1, source, tmp, dest)
    move(n-1, tmp, source, dest)

source = HanoiStack([4,3,2,1])
destination = HanoiStack([])
tmp = HanoiStack([])

try:
    move(4, source, tmp, destination)

    print 'source: ', source.list
    print 'dest: ', destination.list
    print 'tmp: ',tmp.list

except StandardError as e:
    print 'Error: ' + e.message
