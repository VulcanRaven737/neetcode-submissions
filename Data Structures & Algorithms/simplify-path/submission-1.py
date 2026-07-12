from collections import deque

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = deque()
        cleaned = path.split('/')

        for vals in cleaned:
            if vals == '' or vals == '.':
                continue
            elif vals == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(vals)

        return "/" + "/".join(stack)