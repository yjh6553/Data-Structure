# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        subtree_count = {}
        res = []

        def dfs(node):
            if not node:
                return "#"
            
            left_subtree = dfs(node.left)
            right_subtree = dfs(node.right)

            subtree_string = f"{node.val},{left_subtree},{right_subtree}"

            subtree_count[subtree_string] = subtree_count.get(subtree_string, 0) + 1

            if subtree_count[subtree_string] == 2:
                res.append(node)
            
            return subtree_string
        

        dfs(root)
        return res