class Solution:
    def simplifyPath(self, path: str) -> str:
        # Create a stack of each command from path
        # If it is command append to the front of the result.
        
        paths = []
        i = 0

        # Create paths list, splitting the input path into meaningful parts
        while i < len(path):
            if path[i] == "/":
                i += 1
            else:
                cur = ""
                while i < len(path) and path[i] != "/":
                    cur += path[i]
                    i += 1
                paths.append(cur)

        # Stack to process the simplified path
        stack = []

        # Process each part of the path
        for command in paths:
            if command == ".":
                # Current directory, do nothing
                continue
            elif command == "..":
                # Move up one directory (pop from stack if not empty)
                if stack:
                    stack.pop()
            else:
                # Valid directory name, add to stack
                stack.append(command)

        # Construct the simplified path
        res = "/" + "/".join(stack)
        return res