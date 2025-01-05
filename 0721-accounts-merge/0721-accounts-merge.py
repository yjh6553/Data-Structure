from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # Union-Find Helper Functions
        def find(email):
            if parent[email] != email:
                parent[email] = find(parent[email])  # Path compression
            return parent[email]
        
        def union(email1, email2):
            root1 = find(email1)
            root2 = find(email2)
            if root1 != root2:
                parent[root1] = root2
                # parent[root2] = root1  # Union operation
        
        parent = {}
        email_to_name = {}

        # Step 1: Initialize Union-Find and map email to name
        for account in accounts:
            name = account[0]
            first_email = account[1]
            for email in account[1:]:
                if email not in parent:
                    parent[email] = email
                union(first_email, email)
                email_to_name[email] = name

        print(parent)
        print(email_to_name)
        # Step 2: Group emails by root
        email_groups = defaultdict(list)
        for email in parent:
            root = find(email)
            email_groups[root].append(email)

        # Step 3: Build the result
        result = []
        for root, emails in email_groups.items():
            result.append([email_to_name[root]] + sorted(emails))

        return result


        
