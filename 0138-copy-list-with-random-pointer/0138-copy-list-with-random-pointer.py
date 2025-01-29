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


        
        # if not head:
        #     return None  # Handle edge case when head is None
        
        # dummy = Node(0)
        # temp = head

        # node_list = []
        # index = 0

        # # Create a list of deep copied nodes with values only
        # while temp is not None:  # Fixed loop condition
        #     new_copy = Node(temp.val)
        #     node_list.append((new_copy, index))
        #     temp = temp.next
        
        # if not node_list:  # Handle edge case when node_list is empty
        #     return None
        
        # dummy.next = node_list[0][0]

        # # Update next pointer
        # for i in range(len(node_list) - 1):  
        #     node_list[i][0].next = node_list[i+1][0]
        
        # # Update random pointer
        # origin = head
        # update = dummy.next
        # while origin is not None:  # Fix incorrect loop condition
        #     if origin.random is not None:
        #         random_index = [i for i, (node, _) in enumerate(node_list) if node.val == origin.random.val]
        #         if random_index:
        #             update.random = node_list[random_index[0]][0]  # Fix assignment to copied node
        #     origin = origin.next
        #     update = update.next  # Move to the next copied node

        # return dummy.next