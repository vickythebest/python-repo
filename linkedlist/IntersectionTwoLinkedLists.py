from node import Node
class IntersectionTwoLinkedLists:
    def __init__(self):
        self.head=None
    
    def getIntersectionNode(self, headA: Node, headB: Node) -> Node:
        listA=headA
        listB=headB

        while listA != listB:
            if listA is None:
                listA=listB
            else:
                listA=listA.next

            if listB is None:
                listB=listA
            else:
                listB=listB.next
        return listA
            


