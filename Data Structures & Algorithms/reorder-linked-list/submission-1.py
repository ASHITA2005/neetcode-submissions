# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    

    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        length = 1
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            length *= 2
        if fast is not None:
            length += 1 
        
        
        prev = None
        next_n = None
        cur = slow.next
        slow.next = None
        while cur :
            next_n = cur.next
            cur.next = prev
            prev = cur
            cur = next_n

        first = head
        second = prev

        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2


        


        

        

        
      


            
        