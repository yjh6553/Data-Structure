class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        neighbors = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        n, m = len(moveTime) - 1, len(moveTime[0]) - 1

        pq = [(0, 0, 0)]
        heapq.heapify(pq)
    
        visited = set()

        dist = [[float('inf')] * (m + 1) for _ in range(n + 1)]
        dist[0][0] = 0

        while pq:
            # print(pq)
            node = heapq.heappop(pq)
            time, x, y = node[0], node[1], node[2]
            if (x, y) == (n, m):
                return time

            if (x, y) in visited:
                continue
            
            visited.add((x,y))
            
            
            # print(f'start a for loop')
            for nei in neighbors:
                new_x = nei[0] + x
                new_y = nei[1] + y
                
                if new_x > n or new_x < 0 or new_y < 0 or new_y > m:
                    continue
                dest_time = moveTime[new_x][new_y]
                
                # print(f'new_x: {new_x}  new_y: {new_y}  time: {dest_time}')
                if time >= dest_time:
                    new_time = time + 1
                else:
                    new_time = dest_time + 1
                
                if new_time < dist[new_x][new_y]:
                    dist[new_x][new_y] = new_time
                    heapq.heappush(pq, (new_time, new_x, new_y))
            
        return -1

