class Solution:
    def maxArea(self, height: List[int]) -> int:
        val = 0
        head = 0
        tail = len(height) - 1

        while(tail > head):
            length = tail - head
            breadth = min(height[head], height[tail])
            area = length * breadth

            if(area > val):
                val = area

            if(height[head] > height[tail]):
                tail -= 1
            else:
                head += 1
                
        return val

        