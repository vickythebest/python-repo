class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.next=None
        self.previous=None

class doublie_linked_list:
    def __init__(self) -> None:
        self.head=None
        self.previous=None
    
    def insert(self,data):
        newNode=Node(data)
        
        if self.head is None:
            self.head=newNode
            newNode.next=None
            newNode.previous=self.head
        else:
            currentNode=self.head
            while currentNode.next is not None:
                currentNode=currentNode.next
                
            currentNode.next=newNode
            currentNode.next.previous=currentNode

    def insertAt(self,data,pos):
        pass

    def delete(self,data):
        currentNode=self.head
        
        if currentNode.data==data:
            self.head=currentNode.next
            currentNode.next.previous=self.head
        
        while currentNode.next is not None:
            if currentNode.data==data:
                currentNode.next.previous=currentNode.previous
                currentNode.previous.next=currentNode.next
            currentNode=currentNode.next

            if currentNode.data==data:
                currentNode.previous.next=None

    def display(self):
        currentNode=self.head
        while currentNode is not None:
            print("->",currentNode.data)
            currentNode=currentNode.next


if __name__=="__main__":
    doublie_linked_list=doublie_linked_list()
    doublie_linked_list.insert(10)
    doublie_linked_list.insert(11)
    doublie_linked_list.insert(12)
    # doublie_linked_list.display()
    doublie_linked_list.delete(12)
    doublie_linked_list.display()
    