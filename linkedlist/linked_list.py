from node import Node

class linkedlist:
    
    def __init__(self) -> None:
        self.head=None
    
    def dispalyList(self):
        print("Dispaly List:")
        current=self.head
        while current:
            print(current.data)
            current=current.next

    def insert(self,data):
        # print(f"Insert: {data} in linkedlist")
        newNode=Node(data)
        if self.head is None:
            self.head=newNode
            return
        lastNode=self.head
        while lastNode.next:
            lastNode=lastNode.next
        lastNode.next=newNode
         
    def insertAtFront(self,data):
        newNode=Node(data)
        if self.head is None:
            print("head is None")
            self.head=newNode
            return
        
        secondNode=self.head
        self.head=newNode
        newNode.next=secondNode


    def isEmpty(self) -> bool:
        if self.head is None:
            return True
        return False
        

    def delete(self,data):
        list=self.head
        print(f"delete:{data} from list current data at front :",list.data)
        if list.data==data:
            self.head=list.next
            return
        
        currentNode=self.head
        previousNode=None
        while currentNode is not Node and currentNode.data != data:
            previousNode=currentNode
            currentNode=currentNode.next

        previousNode.next=currentNode.next   
                
    def displayReverse(self,node):
        currentNode=node
        if currentNode is None:
            return

        self.displayReverse(currentNode.next)
        print(currentNode.data)
    
    def displayRecursive(self):
        self.displayReverse(self.head)

    def removeNthFromEnd(self, n: int) -> Node:
        currentNode=self.head
        lefttNode=self.head

        if not currentNode:
            return self.head
        
        index=0
        delIndex=n
        while currentNode:
            currentNode=currentNode.next
            index+=1
            if index == delIndex:
                lefttNode=lefttNode.next
                delIndex=delIndex+n
        
        lefttNode.next=lefttNode.next.next


    def reverseLinkedlist(self):
        currentNode=self.head
        previous=None

        while currentNode:
            nxt=currentNode.next
            currentNode.next=previous
            previous=currentNode
            currentNode=nxt
        self.head=previous
        return previous


if __name__=="__main__":
    linkedlist= linkedlist()
    linkedlist.insert(10)
    linkedlist.insert(20)
    linkedlist.insert(130)
    # linkedlist.insertAtFront(5)
    linkedlist.insert(150)
    
    # linkedlist.delete(5)
    # linkedlist.delete(130)
    # print(linkedlist.isEmpty())
    # linkedlist.dispalyList()
    # linkedlist.displayRecursive()
    # linkedlist.removeNthFromEnd(2)
    linkedlist.reverseLinkedlist()
    linkedlist.dispalyList()
