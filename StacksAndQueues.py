# Filename: StacksAndQueues.py
# Author: Gan Jing Ying
# Created: 20130827
# Modified: 20130827
# Description: Program demonstrates how to create a stack and a queue as well as
# provides details on what each method does

class Stack:

    # initializes the stack by creating an empty list
    def __init__(self):
        self.items = []

    # checks if the stack is empty
    # returns a Boolean value (True or False)
    def isEmpty(self):
        return self.items == []

    # adds a new item to the top of the stack
    def push(self, item):
        self.items.append(item)

    # removes the top item on the stack
    # returns the item
    def pop(self):
        return self.items.pop()

    # returns the first item on the stack but does not remove it
    def peek(self):
        return self.items[-1]

    # finds the number of items in the stack
    def size(self):
        return len(self.items)

class Queue:

    # initializes the queue by creating an empty list
    def __init__(self):
        self.items = []

    # checks if the queue is empty
    # returns a Boolean value (True or False)
    def isEmpty(self):
        return self.items == []

    # adds a new item to the back of the queue
    def enqueue(self, item):
        self.items.insert(0, item)

    # removes the first item in the queue
    # returns the item
    def dequeue(self, item):
        return self.items.pop()

    # finds the number of items in the queue
    def size(self):
        return len(self.items)
