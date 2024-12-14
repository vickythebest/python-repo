from node import Node

class circle_linked_list:
    def __init__(self) -> None:
        self.head=None
    
    def insert(self,data):
        newNode=Node(data)
        if self.head==None:
            self.head=newNode
            newNode.next=self.head
        
        currentnode=self.head
        while currentnode.next is not self.head:
            currentnode=currentnode.next 
        currentnode.next=newNode
        newNode.next=self.head
        

    def display(self):
        currentNode=self.head
        while True:
            print(currentNode.data)
            currentNode=currentNode.next
            if currentNode is self.head:
                break
    
    def hasCycle(self) -> Node:
        currentNode=self.head
        secondNode=self.head
        if not currentNode:
            return currentNode
        
        if not secondNode.next:
            return currentNode
        
        while secondNode and secondNode.next:
            secondNode=secondNode.next.next
            currentNode=currentNode.next
            if currentNode == secondNode:
                return secondNode                

    def detectCycle(self) -> Node:
        fast=self.hasCycle()
        if not fast:
            return None
        print("hasCycle",fast.data)
        slow=self.head
        while slow!=fast:
                                                                                        \
            fast=fast.next
        return slow.data

if __name__=="__main__":
    circle_linked_list=circle_linked_list()
    circle_linked_list.insert(3)
    circle_linked_list.insert(2)
    circle_linked_list.insert(0)
    circle_linked_list.insert(-4)
    # circle_linked_list.display()
    # circle_linked_list.printReverse()
    # circle_linked_list.printReverseWithStack()
    # print(circle_linked_list.hasCycle())
    print(circle_linked_list.detectCycle())