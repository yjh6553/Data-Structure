class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        index = []
        for i in range(len(s)):
            if s[i] == '|':
                index.append(i)
        res = []
        
        for q in queries:

            if q[1] - q[0] > 1:
                l_b = self.binary_search(index,q[0],0)#Find lower bound (it will return same position if present else first greater)
                u_b = self.binary_search(index,q[1],1)#Find upper bound(it will return same position if present else first smaller)
                
                if l_b >= u_b:
                    res.append(0)
                    continue
                
                count = index[u_b] - index[l_b] - (u_b - l_b - 1) - 1
                res.append(count)
            else:
                res.append(0)
        return res
        
    def binary_search(self,index,val,b):
        l = 0
        h = len(index) - 1
        
        while l<=h:
            mid = (l+h)//2
            
            if index[mid] == val:
                return mid # If positon matches with given position
            elif index[mid] > val:
                h = mid - 1
            else:
                l = mid + 1 
                
        if b == 0:
            return l
        else:
            return h