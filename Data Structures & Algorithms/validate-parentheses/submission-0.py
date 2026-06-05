class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        if(len(s) <= 1):
            return False

        for i in s:
            if(i == "(" or i == "[" or i == "{"):
                stack.append(i)
            else:
                if(len(stack) == 0):
                    return False

                y = stack.pop()

                if(i == ")" and y != "(" or i == "}" and y != "{" or i == "]" and y != "["):
                    return False

        if len(stack) == 0:
            return True 
        return False
        