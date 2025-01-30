"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        if not root:
            return None

        # BFS
        temp = root
        q = deque([root])

        copy_map = {}

        # BFS to go through all the elements
        while q:
            node = q.popleft()
            copy_map[node] = Node(node.val)
            if len(node.children):
                for child in node.children:
                    q.append(child)
        
        # Another BFS to update children accordingly
        q_1 = deque([root])

        while q_1:
            origin = q_1.popleft()
            copy_node = copy_map[origin]
            if len(origin.children):
                for origin_child in origin.children:
                    copy_node.children.append(copy_map[origin_child])
                    q_1.append(origin_child)
        
        return copy_map[root]
        
                