class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        out = path.split("/")

        for i in out:
            if(i == '..'):
                if(stack):
                    stack.pop()
            elif(i == '.' or i == ""):
                pass
            else:
                stack.append(i)

        return "/"+"/".join(stack)           


        