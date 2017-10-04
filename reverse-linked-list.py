class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

head = Node(1, Node(2, Node(3, Node(4))))

def display(head):
    msg = ''
    while head:
        msg += str(head.data)
        if head.next:
            msg += '->'
        head = head.next
    return msg

def reverse_list(head, tail=None):
    while head:
        head.next, tail, head = tail, head, head.next
    return tail

print(display(head))
print(display(reverse_list(head)))
