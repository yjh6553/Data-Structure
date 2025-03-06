class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.endWord = False
    
    def insert(self, key: str):
        cur = self
        for c in key:
            index = ord(c) - ord('a')
            if cur.children[index] is None:
                cur.children[index] = TrieNode()
            cur = cur.children[index]
        cur.endWord = True

    def search_prefix(self, s: str, start: int):
        """Returns all valid word end indices in the trie starting from index `start`."""
        cur = self
        result = []
        for i in range(start, len(s)):
            index = ord(s[i]) - ord('a')
            if cur.children[index] is None:
                break
            cur = cur.children[index]
            if cur.endWord:
                result.append(i)  # Store valid word end index
        return result

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        trie = TrieNode()

        for word in dictionary:
            trie.insert(word)
        
        n = len(s)
        memo = {}

        def dfs(i: int) -> int:
            # Base Case
            if i == n:
                return 0
            if i in memo:
                return memo[i]

            res = 1 + dfs(i + 1)

            for end in trie.search_prefix(s, i):
                res = min(res, dfs(end + 1))
            
            memo[i] = res
            return res

        return dfs(0)
        
                
        
            


        
