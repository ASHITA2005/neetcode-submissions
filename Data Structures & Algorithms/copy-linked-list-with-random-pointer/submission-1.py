"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    
            
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        new_head = Node(-1)
        start = head
        hash_map = {}
        map_old_to_new = {}
        new_start = new_head
        while head:
            val = head.val
            new_head.next = Node(val)
            new_head.random = None    
            if head.random:
                hash_map[new_head.next] = head.random
            
            map_old_to_new[head] = new_head.next

            new_head = new_head.next
            head = head.next
        head = start
        new_head = new_start.next

        while new_head:
            if new_head in hash_map:
                new_head.random = map_old_to_new[hash_map[new_head]]
            new_head = new_head.next
            

        return new_start.next
        