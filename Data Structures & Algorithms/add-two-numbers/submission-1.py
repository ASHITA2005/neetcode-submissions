# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        c = 0
        s = 0
        new_head = ListNode(-1)
        start = new_head
        while l1 and l2:

            s = l1.val + l2.val + c
            c = s // 10
            s = s % 10 
            #print(s)
            new_head.next = ListNode(s)
            new_head = new_head.next
            l1 = l1.next
            l2 = l2.next
        if c:
            if not l1 and not l2:
                new_head.next = ListNode(c)
                return start.next

            while l1:
                s = l1.val+ c
                c = s // 10
                s = s % 10
                #print(s)
                new_head.next = ListNode(s)
                new_head = new_head.next
                l1 = l1.next

            while l2:
                s = l2.val + c
                c = s // 10
                s = s % 10
               #print(s)
                new_head.next = ListNode(s)
                new_head = new_head.next
                l2 = l2.next
            if c :
                new_head.next = ListNode(c)
            
            

        else:
            if l1:
                new_head.next = l1
            if l2:
                new_head.next = l2
        return start.next





        