# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete_set = set(to_delete)
        res = []
        
        def dfs(node, is_root):
            if not node:
                return None
            
            # Determine if the current node is a root of a subtree
            root_deleted = node.val in to_delete_set
            if is_root and not root_deleted:
                res.append(node)
            
            # Recursively process children
            node.left = dfs(node.left, root_deleted)
            node.right = dfs(node.right, root_deleted)
            
            # Return None if the node is deleted, otherwise return the node
            return None if root_deleted else node
        
        dfs(root, True)
        return res


