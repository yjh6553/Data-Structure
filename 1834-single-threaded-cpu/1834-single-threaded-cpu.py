class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        res = []
        available_task = []
        heapq.heapify(available_task)
        tasks = [(enq, proc, i) for i, (enq, proc) in enumerate(tasks)]
        tasks.sort()
        
        time = 0
        i = 0  # pointer for tasks

        while i < len(tasks) or available_task:
            # Add all tasks available by current time
            while i < len(tasks) and tasks[i][0] <= time:
                enq, proc, idx = tasks[i]
                heapq.heappush(available_task, (proc, idx))
                i += 1

            if available_task:
                proc, idx = heapq.heappop(available_task)
                time += proc
                res.append(idx)
            else:
                # Jump time to next task's enqueue time
                if i < len(tasks):
                    time = tasks[i][0]

        return res