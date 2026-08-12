class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}

        for num in nums:
            if num not in counter:
                counter[num] = 0
            counter[num] += 1

        freq_list = sorted(counter.items(), key = lambda item: item[1], reverse = True)
        returnable = []

        for _ in range(k):
            returnable.append(freq_list[_][0])

        return returnable
