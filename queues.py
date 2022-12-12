
from collections import deque

class Queue:
    def __init__(self):
        self._elements = deque()

    def enqueue(self, element):
        self._elements.append(element)

    def dequeue(self):
        return self._elements.popleft()
        
fifo = Queue()
fifo.enqueue("1st")
fifo.enqueue("2nd")
fifo.enqueue("3rd")

print(fifo.dequeue())

print(fifo.dequeue())

print(fifo.dequeue())

print("\n--___•___--___•___--___•___--___•___--___•___--\n")

#now trying lifo instead of fifo          
lifo = []

lifo.append("1st")
lifo.append("2nd")
lifo.append("3rd")

print(lifo.pop())

print(lifo.pop())

print(lifo.pop())
