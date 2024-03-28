from list_node import ListNode
def addTwoNumbers(l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        result=ListNode()
        current=result
        cary=0
        while l1 is not None and l2 is not None:
            
            sum=l1.val+l2.val
            if sum//10==1:
                cary=1
                current.next=ListNode(0)
                current=current.next
            else:
                current.next=ListNode(l1.val+l2.val+cary)
                current=current.next
            
            l1=l1.next
            l2=l2.next
        
        while result is not None:
             print(result.val)
             result=result.next

l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))
addTwoNumbers(l1,l2)