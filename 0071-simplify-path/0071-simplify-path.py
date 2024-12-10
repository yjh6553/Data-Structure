class Solution:
    def simplifyPath(self, path: str) -> str:
        # Create a stack of each command from path
        # If it is command append to the front of the result.
        
         # Split the path by "/" and process each part
        paths = path.split("/")

        stack = []
        for directory in paths:
            if directory == "" or directory == ".":  # Skip empty or current directory
                continue
            elif directory == "..":
                if stack:  # Go up one directory if possible
                    stack.pop()
            else:
                stack.append(directory)
        
         # Construct the simplified path
        res = "/" + "/".join(stack)
        return res