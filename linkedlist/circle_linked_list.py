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
    
    def displayRecursive(self,node):
        if node.next is not self.head:
            self.displayRecursive(node.next)
        print(node.data)
    
    def printReverse(self):
        self.displayRecursive(self.head)

    def printReverseWithStack(self):
        currentNode=self.head
        stack=[]

        while True:
            stack.append(currentNode.data)
            currentNode=currentNode.next
            if currentNode == self.head:
                break
        
        while stack:
            print(stack.pop())


            

if __name__=="__main__":
    circle_linked_list=circle_linked_list()
    circle_linked_list.insert(1)
    circle_linked_list.insert(2)
    circle_linked_list.insert(3)
    # circle_linked_list.display()
    # circle_linked_list.printReverse()
    circle_linked_list.printReverseWithStack()