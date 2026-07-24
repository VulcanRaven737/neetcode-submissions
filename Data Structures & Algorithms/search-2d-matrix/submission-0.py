class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix) - 1
        cols = len(matrix[0]) - 1
        top = 0 
        bottom = rows 

        while top <= bottom:
            mid = (top + bottom) // 2

            if target > matrix[mid][-1]:
                top = mid + 1
            elif target < matrix[mid][0]:
                bottom = mid - 1
            else:
                break
        
        mid = (top + bottom) // 2
        print(mid)

        l, r = 0, cols

        while l <= r:
            m = l + (r - l) // 2

            if target > matrix[mid][m]:
                l = m + 1
            elif target < matrix[mid][m]:
                r = m - 1
            else:
                return True

        return False