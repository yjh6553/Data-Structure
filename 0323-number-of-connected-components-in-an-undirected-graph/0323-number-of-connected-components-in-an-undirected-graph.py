class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        hashMap=defaultdict(list)
        for x,y in edges:
            hashMap[x].append(y)
            hashMap[y].append(x)
        visited=set()
        count=0
        for index in range(n):
            if index not in visited:
                self.dfsHelper(index, edges, visited, hashMap)
                count+=1
        return count
    
    def dfsHelper(self, index, edges, visited, hashMap):
        if index in visited:
            return
        visited.add(index)
        for neighbor in hashMap[index]:
            self.dfsHelper(neighbor, edges, visited, hashMap)