class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for chars in s:
            if chars == ']':
                temp = ''
                number = ''

                while stack[-1] != '[':
                    temp = stack.pop() + temp
                stack.pop()

                while stack and stack[-1].isdigit():
                    number = stack.pop() + number

                stack.append(int(number) * temp)
            else:
                stack.append(chars)

        return "".join(stack)     
            
        