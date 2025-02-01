class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)  # Convert list to set for fast lookup
        if endWord not in wordSet:
            return 0

        queue = deque([(beginWord, 1)])  # BFS queue storing (word, steps)

        while queue:
            word, steps = queue.popleft()

            if word == endWord:
                return steps

            for i in range(len(word)):
                original = word[i]
                for ch in range(26):  # Check all possible single character changes
                    transformed = word[:i] + chr(ord('a') + ch) + word[i + 1:]
                    if transformed in wordSet:
                        wordSet.remove(transformed)  # Avoid revisiting
                        queue.append((transformed, steps + 1))
        
        return 0  # If no valid transformation is found