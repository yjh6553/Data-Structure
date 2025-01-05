class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_to_name = {}
        graph = defaultdict(list)

        # Build the graph
        for account in accounts:
            name = account[0]
            emails = account[1:]
            for i in range(len(emails)):
                email_to_name[emails[i]] = name
                if i > 0:
                    graph[emails[i]].append(emails[i - 1])
                    graph[emails[i - 1]].append(emails[i])

        # BFS function to traverse the graph
        def bfs(email, visited, emails):
            queue = deque([email])
            visited.add(email)
            while queue:
                current = queue.popleft()
                emails.append(current)
                for neighbor in graph[current]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)

        visited = set()
        result = []

        # Traverse each email and group them
        for email in email_to_name:
            if email not in visited:
                emails = []
                bfs(email, visited, emails)
                result.append([email_to_name[email]] + sorted(emails))

        return result