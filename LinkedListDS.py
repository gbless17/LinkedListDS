from LinkedListDS.Node import Node

class LinkedListDS(object):

    def __init__(self):
        self.head = None 
        self.counter = 0
    #O(N)
    def traverseList(self):
        actualNode = self.head
        print("Scaffolding", actualNode)
        print("Link", actualNode.data)
        print("SomethingElse", actualNode.nextNode)
        print("Pls_Work", actualNode.nextNode.data)

        while actualNode is not None:
            print("%d " % actualNode.data)
            actualNode = actualNode.nextNode
    #O(1)
    def insertStart(self, data):

        self.counter += 1

        newNode = Node(data)

        if not self.head:
            self.head = newNode
        else:
            newNode.NextNode = self.head
            self.head = newNode
    #O(1) instead of O(N)
    def size(self):
        return self.counter

    #O(N) !!!
    def insertEnd(self, data):

        if self.head is None:
            self.insertStart(data)
            return
        self.counter +=1

        newNode = Node(data)
        actualNode = self.head
        

        while actualNode.nextNode is not None:
            actualNode.nextNode = newNode
        actualNode.nextNode = newNode

    def remove(self,data):
        self.counter -=1

        if self.head:
            if data == self.head.data:
                self.head = self.head.nextNode
            else:
                self.head.remove(data, self.head)

