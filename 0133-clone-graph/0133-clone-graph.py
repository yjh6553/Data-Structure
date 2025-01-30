"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        clone_graph = {}

        def dfs(node):
            if node is None:
                return None
            if node in clone_graph:
                return clone_graph[node]
            
            clone = Node(node.val)
            clone_graph[node] = clone

            for neighbor in node.neighbors:
                clone.neighbors.append(dfs(neighbor))
            
            return clone


        return dfs(node)
        