# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        stack = [root]
        visited = set()
        res = 0
        while stack:
            node = stack.pop()
            if low <= node.val <= high:
                res += node.val
                print(node.val)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            elif node.val > high:
                if node.left:
                    stack.append(node.left)
            elif node.val < low:
                if node.right:
                    stack.append(node.right)
        return res