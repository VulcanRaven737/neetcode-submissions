# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        arr1 = []
        sub = []

        def dfs(root, arr):
            if not root:
                arr.append("$None")
                return

            arr.append("$"+str(root.val))
            dfs(root.left, arr)
            dfs(root.right, arr)

        dfs(root, arr1)
        dfs(subRoot, sub)
        
        print(arr1)
        print(sub)

        return "".join(sub) in "".join(arr1)