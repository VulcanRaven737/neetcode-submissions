class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        head = 0
        tail = len(numbers) - 1

        while(tail > head):
            sums = numbers[head] + numbers[tail]
            if (sums == target):
                return [head+1, tail+1]
            elif (sums > target):
                tail -= 1
            elif (sums < target):
                head += 1

        