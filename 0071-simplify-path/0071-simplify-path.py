class Solution:
    def simplifyPath(self, path: str) -> str:
        # Create a stack of each command from path
        # If it is command append to the front of the result.
        
        paths = []
        i = 0

        #create paths list, get rid of "/"s
        while i < len(path):
            if path[i] == "/":
                i += 1
            else:
                cur = ""
                while i < len(path) and path[i] != "/":
                    cur = cur + path[i]
                    i += 1
                paths.append(cur)
    

        stack = []
        for command in paths:
            if command == ".":
                continue
            elif command == "..":
                if stack: # there is more commands
                    stack.pop()
            else:
                stack.append(command)

        
         # Construct the simplified path
        res = "/" + "/".join(stack)
        return res