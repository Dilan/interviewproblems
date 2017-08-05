import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from lib.stack import Stack

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

def solution(items):
    source = HanoiStack(items)
    destination = HanoiStack([])
    tmp = HanoiStack([])
    
    move(len(items), source, tmp, destination)
    
    print('Destination:', destination.list)
    
    return True
