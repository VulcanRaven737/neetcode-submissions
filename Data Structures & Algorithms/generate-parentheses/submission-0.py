class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        stack = []

        def backtrack(string, open, closed):
            if len(string) == 2*n:
                stack.append(string)
                return

            if(open < n):
                backtrack(string + "(", open+1, closed)
            if(closed < open):
                backtrack(string + ")", open, closed+1)

        backtrack("", 0, 0)

        return stack
