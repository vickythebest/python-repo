from node import Node

class insertionSortList:
    def __init__(self) -> None:
        self.head=None

    def insert(self,data):
        newNode=Node(data)
        if self.head is None:
            self.head=newNode
            newNode.next=self.head
        else:
            currentnode=self.head
            while currentnode.next is not self.head:
                currentnode=currentnode.next 
            currentnode.next=newNode
            newNode.next=self.head

    def display(self):
        if not self.head:
            print("List is empty")
            return
        
        currentNode=self.head
        while True:
            print(currentNode.data)
            currentNode=currentNode.next
            if currentNode is self.head:
                break
    
    def insertionSort(self):
        if not self.head or self.head.next == self.head:
            print("blank")
            return  # List is empty or has only one node
        sorted_head=self.head
        current=self.head.next
        sorted_head.next=sorted_head

        while current!=self.head:
            next_node=current.next
            
            if sorted_head.data> current.data:
                current.next=sorted_head
                sorted_head=current
            else:
                prv=sorted_head
                while prv.next and prv.next.data<current.data:
                    prv=prv.next
                current.next=prv.next
                prv.next=current
            current=next_node
        self.head=sorted_head.head
        # return self.head

if __name__== "__main__":
    list=insertionSortList()
    list.insert(4)
    list.insert(2)
    list.insert(1)
    list.insert(3)
    
    list.display()
    list=insertionSortList()
    list.insertionSort()
    list.display()