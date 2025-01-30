# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random

class NodeCopy:
    def __init__(self, val=0, left=None, right=None, random=None):
        self.val = val
        self.left = left
        self.right = right
        self.random = random

class Solution:
    def copyRandomBinaryTree(self, root: 'Optional[Node]') -> 'Optional[NodeCopy]':
        if not root:
            return None

        q = deque([root])
        copy_map = {root: NodeCopy(root.val)}  # Store copies of original nodes
        
        # First pass: Copy all nodes and link left/right pointers
        while q:
            node = q.popleft()
            copy = copy_map[node]  # Get copied node

            if node.left:
                if node.left not in copy_map:
                    copy_map[node.left] = NodeCopy(node.left.val)
                copy.left = copy_map[node.left]
                q.append(node.left)
            
            if node.right:
                if node.right not in copy_map:
                    copy_map[node.right] = NodeCopy(node.right.val)
                copy.right = copy_map[node.right]
                q.append(node.right)

        # Second pass: Assign random pointers
        q = deque([root])
        while q:
            node = q.popleft()
            copy = copy_map[node]  # Get copied node
            
            if node.random:
                copy.random = copy_map[node.random]

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        return copy_map[root]  # Return the copied root


        # # BFS

        # q = deque([root])
        # copy_map = {} # Key: Original, Value: Copied Version
        # index = [root] #Store original nodes by its index

        # # Create a copy nodes and update index list
        # while q:
        #     node = q.popleft()
        #     if not node.left:
        #         index.append(None)
        #     else:
        #         copy = Node(node.val)
        #         copy_map[node] = copy
        #         index.append(node.left)
        #         q.append(node.left)
            
        #     if not node.right:
        #         index.append(None)
        #     else:
        #         copy = Node(node.val)
        #         copy_map[node] = copy
        #         index.append(node.right)
        #         q.append(node.right)
        
        # q1 = deque([root])
        # while q1:
        #     origin = q1.popleft()
        #     if origin.random:
