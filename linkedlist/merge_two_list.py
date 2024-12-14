from linked_list import linkedlist
class merge_two_linkedlist():
    def __init__(self) -> None:
        self.head=None

    def mergeList(self,ll1,ll2,start,end):
        l1=ll1.head
        l2=ll2.head

        count=1
        while count < end:
            l1=l1.next
            count+=1
        
        while l2.next:
            l2=l2.next
        
        l2.next=l1
        
        count=1
        l1=ll1.head
        while count < start:
            l1=l1.next
            count+=1
        l1.next=ll2.head

if __name__=="__main__":
    l1= linkedlist()
    l1.insert(1)
    l1.insert(2)
    l1.insert(3)
    l1.insert(4)
    l1.insert(5)
    
    l2= linkedlist()
    l2.insert(6)
    l2.insert(7)
    l2.insert(8)
    l2.insert(9)
    l2.insert(10)

    m=merge_two_linkedlist()
    m.mergeList(l1,l2)
    l1.dispalyList()