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
        if not head:
            return None
        
        # Step 1: Create a mapping from original nodes to copied nodes
        node_map = {}
        temp = head
        
        # First pass: Create new nodes and map them
        while temp:
            node_map[temp] = Node(temp.val)
            temp = temp.next
        
        # Second pass: Assign next and random pointers
        temp = head
        while temp:
            if temp.next:
                node_map[temp].next = node_map[temp.next]
            if temp.random:
                node_map[temp].random = node_map[temp.random]
            temp = temp.next
        
        return node_map[head]



        