class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        checker = defaultdict(list)
        for word in strs:
            sorts = "".join(sorted(word))

            checker[sorts].append(word)
        
        return list(checker.values())

        