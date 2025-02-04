class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        goal = (n*n)
        res = 0

        # BFS
        q = deque([(1, 0)]) # (pos, steps)
        visited = set([1])

        while q:
            curr, step = q.popleft()
            for i in range(1, 7): # 1 - 6 die 
                newCurr = curr + i
                if newCurr > n * n:
                    break
                row, col = self.calculatePosition(newCurr, n)

                if board[row][col] != -1:
                    newCurr = board[row][col]

                if newCurr == n * n:
                    return step + 1

                if newCurr not in visited:
                    visited.add(newCurr)
                    q.append((newCurr, step + 1))

        return -1
        


    def calculatePosition(self, pos: int, n: int) -> (int, int):
        index = pos - 1 
        row = index // n
        col = index % n 

        if row % 2 != 0:
            col = n - col - 1
        row = n - 1 - row
        return row, col
