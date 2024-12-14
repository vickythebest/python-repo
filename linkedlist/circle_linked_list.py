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

    def hasCycle(self) -> bool:
        currentNode=self.head
        secondNode=self.head
        if not currentNode:
            return False
        
        if not secondNode.next:
            return False
        
        while currentNode and secondNode.next:
            if secondNode.next.next:
                secondNode=secondNode.next.next
                if currentNode == secondNode:
                    return True                
            currentNode=currentNode.next
 
        return False

    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=head
        fast=head
        
        if not slow:
            print("first edge case")
            return slow
        
        if fast.next ==slow:
            print("second edge case")
            return fast.next
        index = 0
        while slow and fast.next:
            print("while",index,slow.val)
            if fast.next.next:
                print("fast.next")
                fast=fast.next.next
                if slow.val ==fast.val:
                    print("cycle lnkedlist at index :",index)
                    return fast
            slow=slow.next
            index+=1
                
        return None
            


            

if __name__=="__main__":
    circle_linked_list=circle_linked_list()
    circle_linked_list.insert(3)
    circle_linked_list.insert(2)
    circle_linked_list.insert(0)
    circle_linked_list.insert(-4)
    # circle_linked_list.display()
    # circle_linked_list.printReverse()
    # circle_linked_list.printReverseWithStack()
    print(circle_linked_list.hasCycle())