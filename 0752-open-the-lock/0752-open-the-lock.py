class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # BFS
        root = "0000"
        if root in deadends:
            return -1
        if root == target:
            return 0
            
        q = deque()
        q.append(root)
        deadends = set(deadends)
        deadends.add("0000")
       
        current_step = 1
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                # childs = computePossibleCombs(node)
                
                for i in range(4):
                    newComb = list(node)
                    digit = int(newComb[i]) + 10
                    upOne = (digit + 1) % 10
                    downOne = (digit - 1) % 10

                    newComb[i] = str(upOne)
                    possibleComb = "".join(newComb)
                    if possibleComb not in deadends:
                        q.append(possibleComb)
                        deadends.add(possibleComb)
                    if possibleComb == target:
                        return current_step

                    newComb[i] = str(downOne)
                    possibleComb = "".join(newComb)
                    if possibleComb not in deadends:
                        q.append(possibleComb)
                        deadends.add(possibleComb)
                    if possibleComb == target:
                        return current_step

            current_step += 1

        return -1        


        