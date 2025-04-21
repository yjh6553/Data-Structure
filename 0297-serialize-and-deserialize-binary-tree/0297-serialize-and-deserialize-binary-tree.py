# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return '[]'
        
        q = deque([root])
        res = []
        while q:
            node = q.popleft()
            
            if node:
                q.append(node.left)
                q.append(node.right)
                res.append(node.val)
            else:
                res.append(None)
        return str(res)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """    
        if data == '[]':
            return None
        
        data_list = eval(data)
        root = TreeNode(data_list[0])
        i = 1
        q = deque([root])

        while q and i < len(data_list):
            node = q.popleft()
            if i < len(data_list) and data_list[i] is not None:
                node.left = TreeNode(data_list[i])
                q.append(node.left)
            i += 1
            if i < len(data_list) and data_list[i] is not None:
                node.right = TreeNode(data_list[i])
                q.append(node.right)
            i += 1
            
        return root        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))